import pandas as pd


def load_csv(file_path) -> pd.DataFrame:
    """Load a CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path, encoding="latin1")


def validate_dataframe(df: pd.DataFrame) -> None:
    """Validate that the DataFrame contains data."""
    if df.empty:
        raise ValueError("The CSV file is empty.")

    if df.columns.empty:
        raise ValueError("The CSV file has no columns.")