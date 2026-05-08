import pandas as pd


def get_demo_qpcr_data():
    data = [
        {"sample": "NC", "gene": "ACTB", "ct": 18.2},
        {"sample": "NC", "gene": "Target", "ct": 24.6},
        {"sample": "WT", "gene": "ACTB", "ct": 18.5},
        {"sample": "WT", "gene": "Target", "ct": 22.8},
        {"sample": "Sample_1", "gene": "ACTB", "ct": 18.4},
        {"sample": "Sample_1", "gene": "Target", "ct": 21.9},
        {"sample": "Sample_2", "gene": "ACTB", "ct": 18.1},
        {"sample": "Sample_2", "gene": "Target", "ct": 23.2},
    ]
    return pd.DataFrame(data)


def get_demo_ddpcr_data():
    data = [
        {"sample": "NC", "copies_per_ul": 120},
        {"sample": "WT", "copies_per_ul": 210},
        {"sample": "Sample_1", "copies_per_ul": 560},
        {"sample": "Sample_2", "copies_per_ul": 430},
    ]
    return pd.DataFrame(data)


def calc_qpcr_relative_expression(df, ref_gene="ACTB", control_sample="NC"):
    required_cols = {"sample", "gene", "ct"}
    missing_cols = required_cols - set(df.columns)

    if missing_cols:
        raise ValueError(
            "qPCR 数据缺少必要字段: "
            + ", ".join(sorted(missing_cols))
            + "。需要包含 sample, gene, ct。"
        )

    work = df.copy()
    work["ct"] = pd.to_numeric(work["ct"], errors="coerce")
    work = work.dropna(subset=["ct"])

    pivot = work.pivot_table(
        index="sample",
        columns="gene",
        values="ct",
        aggfunc="mean"
    ).reset_index()

    if ref_gene not in pivot.columns:
        raise ValueError(f"找不到内参基因: {ref_gene}")

    target_cols = [
        col for col in pivot.columns
        if col not in ["sample", ref_gene]
    ]

    if not target_cols:
        raise ValueError("未找到目标基因列。")

    target_gene = target_cols[0]

    pivot["delta_ct"] = pivot[target_gene] - pivot[ref_gene]

    control_rows = pivot[pivot["sample"] == control_sample]

    if control_rows.empty:
        raise ValueError(f"找不到对照样本: {control_sample}")

    control_delta_ct = control_rows["delta_ct"].iloc[0]

    pivot["delta_delta_ct"] = pivot["delta_ct"] - control_delta_ct
    pivot["relative_expression"] = 2 ** (-pivot["delta_delta_ct"])

    result = pivot[
        [
            "sample",
            ref_gene,
            target_gene,
            "delta_ct",
            "delta_delta_ct",
            "relative_expression"
        ]
    ].copy()

    result = result.rename(
        columns={
            ref_gene: f"{ref_gene}_ct",
            target_gene: f"{target_gene}_ct"
        }
    )

    return result.round(4)


def calc_ddpcr_summary(df):
    required_cols = {"sample", "copies_per_ul"}
    missing_cols = required_cols - set(df.columns)

    if missing_cols:
        raise ValueError(
            "ddPCR 数据缺少必要字段: "
            + ", ".join(sorted(missing_cols))
            + "。需要包含 sample, copies_per_ul。"
        )

    work = df.copy()
    work["copies_per_ul"] = pd.to_numeric(
        work["copies_per_ul"],
        errors="coerce"
    )
    work = work.dropna(subset=["copies_per_ul"])

    result = work.groupby("sample", as_index=False).agg(
        mean_copies_per_ul=("copies_per_ul", "mean"),
        replicate_count=("copies_per_ul", "count")
    )

    return result.round(4)


def merge_qpcr_ddpcr(qpcr_result, ddpcr_result):
    merged = pd.merge(
        qpcr_result,
        ddpcr_result,
        on="sample",
        how="outer"
    )

    return merged.round(4)
