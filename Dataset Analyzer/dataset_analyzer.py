import argparse

import numpy as np
import pandas as pd


def load_dataset(file_path):
    return pd.read_csv(file_path)


def validate_file(file_path):
    if not file_path.lower().endswith(".csv"):
        raise ValueError("Only CSV files are supported.")


def print_header(title):
    print()
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)


def show_overview(df, file_path):
    print_header("DATASET OVERVIEW")

    print(f"File       : {file_path}")
    print(f"Rows       : {df.shape[0]}")
    print(f"Columns    : {df.shape[1]}")


def show_columns(df):
    print_header("COLUMNS")

    for index, column in enumerate(df.columns, start=1):
        print(f"{index:>2}. {column}")


def show_first_row(df):
    print_header("FIRST ROW")

    print(df.head(1).to_string(index=False))


def show_schema(df):
    print_header("SCHEMA")

    schema = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str).values
    })

    print(schema.to_string(index=False))


def calculate_missing_percentage(df):
    missing_count = df.isnull().sum()
    missing_percentage = (missing_count / len(df)) * 100

    return missing_percentage


def show_missing_values(df):
    print_header("MISSING VALUES")

    missing_count = df.isnull().sum()
    missing_percentage = calculate_missing_percentage(df)

    missing_report = pd.DataFrame({
        "Column": df.columns,
        "Missing": missing_count.values,
        "Percentage": missing_percentage.values
    })

    missing_report = missing_report[missing_report["Missing"] > 0]

    if missing_report.empty:
        print("No missing values found.")
        return

    print(
        missing_report.to_string(
            index=False,
            formatters={
                "Percentage": "{:.2f}%".format
            }
        )
    )


def show_statistics(df):
    print_header("NUMERICAL STATISTICS")

    print(df.describe().to_string())


def show_duplicates(df):
    print_header("DUPLICATES")

    duplicate_count = df.duplicated().sum()

    print(f"Duplicate rows : {duplicate_count}")


def show_column_types(df):
    print_header("COLUMN CATEGORIES")

    numerical_columns = df.select_dtypes(
        include=np.number
    ).columns

    string_columns = df.select_dtypes(
        include="str"
    ).columns

    print("Numerical columns:")

    for column in numerical_columns:
        print(f"  - {column}")

    print()
    print("String / categorical columns:")

    for column in string_columns:
        print(f"  - {column}")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze a CSV dataset"
    )

    parser.add_argument(
        "file",
        help="Path to CSV file"
    )

    args = parser.parse_args()

    try:
        validate_file(args.file)
        df = load_dataset(args.file)

    except FileNotFoundError:
        print(f"Error: File not found: {args.file}")
        return

    except ValueError as error:
        print(f"Error: {error}")
        return

    print_header("DATASET ANALYZER")

    show_overview(df, args.file)
    show_columns(df)
    show_first_row(df)
    show_schema(df)
    show_missing_values(df)
    show_statistics(df)
    show_duplicates(df)
    show_column_types(df)


if __name__ == "__main__":
    main()