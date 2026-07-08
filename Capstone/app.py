import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Auto EDA Tool",
    page_icon="📊",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("📊 Automated EDA Tool")

st.markdown("## 👩‍💻 Developed by **Alfina Shaikh**")

st.caption("Capstone Project – Data Analytics")

st.success("✅ App Loaded Successfully")

st.write("Upload any CSV file and get an instant Exploratory Data Analysis (EDA).")

st.divider()

# ---------------- FILE UPLOADER ----------------
uploaded_file = st.file_uploader(
    "📂 Upload your CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("✅ Dataset Loaded Successfully!")

    st.header("📋 Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.subheader("Column Names")
    st.write(df.columns.tolist())

    st.subheader("First 5 Rows")
    st.dataframe(df.head())

    st.subheader("Summary Statistics")
    st.write(df.describe())

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    numeric_columns = df.select_dtypes(include="number").columns

    if len(numeric_columns) > 0:

        selected = st.selectbox(
            "Select Numeric Column",
            numeric_columns
        )

        st.subheader("Histogram")

        fig, ax = plt.subplots(figsize=(8,4))
        sns.histplot(df[selected], kde=True, ax=ax)
        st.pyplot(fig)

        st.subheader("Box Plot")

        fig2, ax2 = plt.subplots(figsize=(8,4))
        sns.boxplot(x=df[selected], ax=ax2)
        st.pyplot(fig2)

        st.subheader("Correlation Heatmap")

        fig3, ax3 = plt.subplots(figsize=(8,6))
        sns.heatmap(
            df[numeric_columns].corr(),
            annot=True,
            cmap="coolwarm",
            ax=ax3
        )

        st.pyplot(fig3)

else:
    st.info("📂 Please upload a CSV file.")

# ---------------- PROCESS FILE ----------------
if uploaded_file is not None:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.success("Dataset Loaded Successfully!")

    # ---------------- DATASET INFO ----------------
    st.header("📋 Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    # ---------------- COLUMN NAMES ----------------
    st.subheader("📌 Column Names")
    st.write(df.columns.tolist())

    # ---------------- FIRST ROWS ----------------
    st.subheader("👀 First 5 Rows")
    st.dataframe(df.head())

    # ---------------- SUMMARY ----------------
    st.subheader("📊 Summary Statistics")
    st.dataframe(df.describe())

    # ---------------- MISSING VALUES ----------------
    st.subheader("❗ Missing Values")
    st.dataframe(df.isnull().sum().rename("Missing Values"))

    # ---------------- NUMERIC COLUMNS ----------------
    numeric_columns = df.select_dtypes(include="number").columns

    if len(numeric_columns) > 0:

        selected_column = st.selectbox(
            "📈 Select a Numeric Column",
            numeric_columns
        )

        # ---------------- HISTOGRAM ----------------
        st.subheader("📊 Histogram")

        fig1, ax1 = plt.subplots(figsize=(8,4))

        sns.histplot(
            df[selected_column],
            kde=True,
            ax=ax1
        )

        st.pyplot(fig1)

        # ---------------- BOXPLOT ----------------
        st.subheader("📦 Box Plot")

        fig2, ax2 = plt.subplots(figsize=(8,4))

        sns.boxplot(
            x=df[selected_column],
            ax=ax2
        )

        st.pyplot(fig2)

        # ---------------- HEATMAP ----------------
        st.subheader("🔥 Correlation Heatmap")

        fig3, ax3 = plt.subplots(figsize=(8,6))

        sns.heatmap(
            df[numeric_columns].corr(),
            annot=True,
            cmap="coolwarm",
            ax=ax3
        )

        st.pyplot(fig3)

    else:
        st.warning("⚠️ No numeric columns found in this dataset.")

# ---------------- NO FILE ----------------
else:

    st.info("👆 Please upload a CSV file to begin.")