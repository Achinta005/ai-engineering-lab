import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and prepare the raw dataset."""

    df = df.copy()

    # Remove leading/trailing whitespace from column names
    df.columns = df.columns.str.strip()

    # Convert date columns
    if "Order Date" in df.columns:
        df["Order Date"] = pd.to_datetime(
            df["Order Date"],
            errors="coerce"
        )

    if "Ship Date" in df.columns:
        df["Ship Date"] = pd.to_datetime(
            df["Ship Date"],
            errors="coerce"
        )

    # Remove completely empty rows
    df = df.dropna(how="all")

    return df

def add_calculated_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Add calculated columns useful for analysis."""

    df = df.copy()

    if {"Sales", "Profit"}.issubset(df.columns):
        df["Profit Margin"] = (
            df["Profit"] / df["Sales"]
        ) * 100

    if {"Order Date", "Sales"}.issubset(df.columns):
        df["Order Year"] = df["Order Date"].dt.year
        df["Order Month"] = df["Order Date"].dt.month
        df["Order Month Name"] = df["Order Date"].dt.month_name()

    return df

def get_summary(df: pd.DataFrame) -> dict:
    """Return key metrics for the dashboard."""

    summary = {
        "total_rows": len(df),
        "total_sales": 0,
        "total_profit": 0,
        "total_quantity": 0,
    }

    if "Sales" in df.columns:
        summary["total_sales"] = df["Sales"].sum()

    if "Profit" in df.columns:
        summary["total_profit"] = df["Profit"].sum()

    if "Quantity" in df.columns:
        summary["total_quantity"] = df["Quantity"].sum()

    return summary