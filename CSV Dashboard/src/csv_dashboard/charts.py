import plotly.express as px
import pandas as pd


def sales_by_region(df: pd.DataFrame):
    """Create a bar chart showing sales by region."""

    data = (
        df.groupby("Region", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    fig = px.bar(
        data,
        x="Region",
        y="Sales",
        title="Sales by Region",
        labels={
            "Region": "Region",
            "Sales": "Total Sales",
        },
    )

    return fig


def sales_by_category(df: pd.DataFrame):
    """Create a bar chart showing sales by category."""

    data = (
        df.groupby("Category", as_index=False)
        .agg(Sales=("Sales", "sum"))
        .sort_values(by="Sales", ascending=False)
    )

    fig = px.bar(
        data,
        x="Category",
        y="Sales",
        title="Sales by Category",
        labels={
            "Category": "Category",
            "Sales": "Total Sales",
        },
    )

    return fig


def profit_by_category(df: pd.DataFrame):
    """Create a bar chart showing profit by category."""

    data = (
        df.groupby("Category", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
    )

    fig = px.bar(
        data,
        x="Category",
        y="Profit",
        title="Profit by Category",
        labels={
            "Category": "Category",
            "Profit": "Total Profit",
        },
    )

    return fig


def sales_over_time(df: pd.DataFrame):
    """Create a line chart showing sales over time."""

    data = (
        df.groupby("Order Date", as_index=False)["Sales"]
        .sum()
        .sort_values("Order Date")
    )

    fig = px.line(
        data,
        x="Order Date",
        y="Sales",
        title="Sales Over Time",
    )

    return fig


def top_products(df: pd.DataFrame, limit: int = 10):
    """Create a chart showing the top products by sales."""

    data = (
        df.groupby("Product Name", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(limit)
    )

    fig = px.bar(
        data,
        x="Sales",
        y="Product Name",
        orientation="h",
        title=f"Top {limit} Products by Sales",
        labels={
            "Product Name": "Product",
            "Sales": "Total Sales",
        },
    )

    return fig