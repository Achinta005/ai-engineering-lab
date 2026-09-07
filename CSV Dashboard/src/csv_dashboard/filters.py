import pandas as pd


def filter_by_region(
    df: pd.DataFrame,
    region: str | None,
) -> pd.DataFrame:
    """Filter data by region."""

    if not region or region == "All":
        return df.copy()

    return df[df["Region"] == region].copy()

def filter_by_category(
    df: pd.DataFrame,
    category: str | None,
) -> pd.DataFrame:
    """Filter data by category."""

    if not category or category == "All":
        return df.copy()

    return df[df["Category"] == category].copy()

def filter_by_values(
    df: pd.DataFrame,
    column: str,
    values: list[str] | None,
) -> pd.DataFrame:
    """Filter a DataFrame column using multiple selected values."""

    if not values:
        return df.copy()

    return df[df[column].isin(values)].copy()

def filter_by_date(
    df: pd.DataFrame,
    start_date,
    end_date,
) -> pd.DataFrame:
    """Filter data between two dates."""

    if "Order Date" not in df.columns:
        return df.copy()

    mask = (
        (df["Order Date"] >= pd.Timestamp(start_date))
        & (df["Order Date"] <= pd.Timestamp(end_date))
    )

    return df[mask].copy()