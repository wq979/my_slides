import streamlit as st
import pandas as pd
from io import StringIO

from compute import (
    get_demo_qpcr_data,
    get_demo_ddpcr_data,
    calc_qpcr_relative_expression,
    calc_ddpcr_summary,
    merge_qpcr_ddpcr,
)


st.set_page_config(
    page_title="qPCR + ddPCR 分析工具",
    layout="wide"
)

st.markdown(
    """
    <style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}

    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 1rem;
        padding-left: 1.8rem;
        padding-right: 1.8rem;
        max-width: 100%;
    }

    h1 {
        font-size: 2rem !important;
        line-height: 1.15 !important;
        margin-bottom: 0.2rem !important;
    }

    h2, h3 {
        font-size: 1.35rem !important;
    }

    [data-testid="stFileUploader"] {
        transform: scale(0.92);
        transform-origin: left top;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def read_uploaded_table(uploaded_file):
    if uploaded_file is None:
        return None

    if uploaded_file.name.endswith(".csv"):
        return pd.read_csv(uploaded_file)

    if uploaded_file.name.endswith(".xlsx"):
        return pd.read_excel(uploaded_file)

    st.error("暂时只支持 CSV 或 XLSX 文件。")
    return None


def make_download_csv(df):
    buffer = StringIO()
    df.to_csv(buffer, index=False, encoding="utf-8-sig")
    return buffer.getvalue()


st.title("qPCR + ddPCR 分析工具")
st.caption("共享一套算法")

tab1, tab2, tab3 = st.tabs(["qPCR", "ddPCR", "合并后"])


with tab1:
    st.subheader("qPCR 相对定量")

    uploaded_qpcr = st.file_uploader(
        "上传 Ct 值表",
        type=["csv", "xlsx"],
        key="qpcr_upload"
    )

    col1, col2 = st.columns(2)

    with col1:
        ref_gene = st.selectbox("内参基因", ["ACTB", "GAPDH"])

    with col2:
        control_sample = st.selectbox("对照样本", ["NC", "WT"])

    use_demo_qpcr = st.checkbox("没有文件时使用示例 qPCR 数据", value=True)

    if st.button("运行 qPCR 分析"):
        qpcr_df = read_uploaded_table(uploaded_qpcr)

        if qpcr_df is None and use_demo_qpcr:
            qpcr_df = get_demo_qpcr_data()

        if qpcr_df is None:
            st.warning("请上传 qPCR 数据文件，或勾选使用示例数据。")
        else:
            result = calc_qpcr_relative_expression(
                qpcr_df,
                ref_gene=ref_gene,
                control_sample=control_sample
            )

            st.success("qPCR 分析完成")
            st.dataframe(result, use_container_width=True)

            st.download_button(
                label="下载 qPCR 结果 CSV",
                data=make_download_csv(result),
                file_name="qpcr_result.csv",
                mime="text/csv"
            )


with tab2:
    st.subheader("ddPCR 拷贝数分析")

    uploaded_ddpcr = st.file_uploader(
        "上传 ddPCR 数据表",
        type=["csv", "xlsx"],
        key="ddpcr_upload"
    )

    use_demo_ddpcr = st.checkbox("没有文件时使用示例 ddPCR 数据", value=True)

    if st.button("运行 ddPCR 分析"):
        ddpcr_df = read_uploaded_table(uploaded_ddpcr)

        if ddpcr_df is None and use_demo_ddpcr:
            ddpcr_df = get_demo_ddpcr_data()

        if ddpcr_df is None:
            st.warning("请上传 ddPCR 数据文件，或勾选使用示例数据。")
        else:
            result = calc_ddpcr_summary(ddpcr_df)

            st.success("ddPCR 分析完成")
            st.dataframe(result, use_container_width=True)

            st.download_button(
                label="下载 ddPCR 结果 CSV",
                data=make_download_csv(result),
                file_name="ddpcr_result.csv",
                mime="text/csv"
            )


with tab3:
    st.subheader("qPCR + ddPCR 合并结果")

    st.info("这里演示将 qPCR 相对表达结果和 ddPCR 拷贝数结果合并展示。")

    if st.button("生成合并示例结果"):
        qpcr_demo = get_demo_qpcr_data()
        ddpcr_demo = get_demo_ddpcr_data()

        qpcr_result = calc_qpcr_relative_expression(
            qpcr_demo,
            ref_gene="ACTB",
            control_sample="NC"
        )

        ddpcr_result = calc_ddpcr_summary(ddpcr_demo)
        merged = merge_qpcr_ddpcr(qpcr_result, ddpcr_result)

        st.success("合并完成")
        st.dataframe(merged, use_container_width=True)

        st.download_button(
            label="下载合并结果 CSV",
            data=make_download_csv(merged),
            file_name="merged_result.csv",
            mime="text/csv"
        )
