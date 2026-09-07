import streamlit as st

from csv_dashboard.data_loader import load_csv, validate_dataframe
from csv_dashboard.transformations import (
    clean_data,
    add_calculated_columns,
    get_summary,
)
from csv_dashboard.filters import (
    filter_by_region,
    filter_by_category,
    filter_by_values,
    filter_by_date,
)
from csv_dashboard.charts import (
    sales_by_region,
    sales_by_category,
    profit_by_category,
    sales_over_time,
    top_products,
)


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="CSV Dashboard",
    page_icon="📊",
    layout="wide",
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📊 CSV Dashboard")
st.write("Upload a CSV file and explore your data interactively.")


# --------------------------------------------------
# File Upload
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"],
)


if uploaded_file is None:
    st.info("Please upload a CSV file to continue.")
    st.stop()


# --------------------------------------------------
# Load Data
# --------------------------------------------------

try:
    df = load_csv(uploaded_file)
    validate_dataframe(df)

except Exception as e:
    st.error(f"Unable to load CSV file: {e}")
    st.stop()


# --------------------------------------------------
# Clean & Transform Data
# --------------------------------------------------

df = clean_data(df)
df = add_calculated_columns(df)


# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------

st.sidebar.header("Filters")


# Region filter
if "Region" in df.columns:
    regions = ["All"] + sorted(df["Region"].dropna().unique().tolist())

    selected_region = st.sidebar.selectbox(
        "Region",
        regions,
    )

else:
    selected_region = "All"


# Category filter
if "Category" in df.columns:
    categories = ["All"] + sorted(
        df["Category"].dropna().unique().tolist()
    )

    selected_category = st.sidebar.selectbox(
        "Category",
        categories,
    )

else:
    selected_category = "All"


# Sub-category filter
if "Sub-Category" in df.columns:
    sub_categories = sorted(
        df["Sub-Category"].dropna().unique().tolist()
    )

    selected_sub_categories = st.sidebar.multiselect(
        "Sub-Category",
        sub_categories,
    )

else:
    selected_sub_categories = []


# Segment filter
if "Segment" in df.columns:
    segments = sorted(
        df["Segment"].dropna().unique().tolist()
    )

    selected_segments = st.sidebar.multiselect(
        "Segment",
        segments,
    )

else:
    selected_segments = []


# Date filter
if "Order Date" in df.columns:

    min_date = df["Order Date"].min().date()
    max_date = df["Order Date"].max().date()

    selected_dates = st.sidebar.date_input(
        "Order Date",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

else:
    selected_dates = None


# --------------------------------------------------
# Apply Filters
# --------------------------------------------------

filtered_df = df.copy()


if selected_region != "All":
    filtered_df = filter_by_region(
        filtered_df,
        selected_region,
    )


if selected_category != "All":
    filtered_df = filter_by_category(
        filtered_df,
        selected_category,
    )


if selected_sub_categories:
    filtered_df = filter_by_values(
        filtered_df,
        "Sub-Category",
        selected_sub_categories,
    )


if selected_segments:
    filtered_df = filter_by_values(
        filtered_df,
        "Segment",
        selected_segments,
    )


if selected_dates and len(selected_dates) == 2:
    filtered_df = filter_by_date(
        filtered_df,
        selected_dates[0],
        selected_dates[1],
    )


# --------------------------------------------------
# Dashboard Summary
# --------------------------------------------------

summary = get_summary(filtered_df)


st.subheader("Overview")


col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Total Sales",
    f"${summary['total_sales']:,.2f}",
)

col2.metric(
    "Total Profit",
    f"${summary['total_profit']:,.2f}",
)

col3.metric(
    "Total Quantity",
    f"{summary['total_quantity']:,}",
)

col4.metric(
    "Total Rows",
    f"{summary['total_rows']:,}",
)


# --------------------------------------------------
# Charts
# --------------------------------------------------

st.subheader("Sales Analysis")


col1, col2 = st.columns(2)


with col1:
    if {"Region", "Sales"}.issubset(filtered_df.columns):
        st.plotly_chart(
            sales_by_region(filtered_df),
            use_container_width=True,
        )


with col2:
    if {"Category", "Sales"}.issubset(filtered_df.columns):
        st.plotly_chart(
            sales_by_category(filtered_df),
            use_container_width=True,
        )


col1, col2 = st.columns(2)


with col1:
    if {"Category", "Profit"}.issubset(filtered_df.columns):
        st.plotly_chart(
            profit_by_category(filtered_df),
            use_container_width=True,
        )


with col2:
    if {"Order Date", "Sales"}.issubset(filtered_df.columns):
        st.plotly_chart(
            sales_over_time(filtered_df),
            use_container_width=True,
        )


# Top Products
if {"Product Name", "Sales"}.issubset(filtered_df.columns):

    st.subheader("Top Products")

    st.plotly_chart(
        top_products(filtered_df),
        use_container_width=True,
    )


# --------------------------------------------------
# Data Preview
# --------------------------------------------------

st.subheader("Filtered Data")

st.dataframe(
    filtered_df,
    use_container_width=True,
)


# --------------------------------------------------
# Download
# --------------------------------------------------

csv_data = filtered_df.to_csv(index=False).encode("utf-8")


st.download_button(
    label="⬇️ Download Filtered CSV",
    data=csv_data,
    file_name="filtered_data.csv",
    mime="text/csv",
)