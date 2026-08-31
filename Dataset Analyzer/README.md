# Dataset Analyzer

A lightweight Python CLI tool for analyzing CSV datasets and generating a structured summary directly in the terminal.

This project is part of my AI Engineering learning journey and is the first project in the **Python & Data Analysis** stage.

## Features

- Load CSV datasets from the command line
- Display dataset dimensions
- List all columns
- Preview the first row
- Display column data types
- Detect missing values
- Calculate missing-value percentages
- Generate numerical summary statistics
- Detect duplicate rows
- Identify numerical and string/categorical columns
- Validate CSV file input
- Handle missing files gracefully
- Generate a clean terminal-based analysis report

## Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **argparse**

## Project Structure

```text
Dataset Analyzer/
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── gender_submission.csv
│
├── notebooks/
│   └── experiments.ipynb
│
├── dataset_analyzer.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd "Dataset Analyzer"
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

#### Linux / macOS

```bash
source .venv/bin/activate
```

#### Windows

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

The analyzer accepts the CSV file path as a command-line argument.

```bash
python dataset_analyzer.py data/train.csv
```

You can analyze any CSV file by providing its path:

```bash
python dataset_analyzer.py path/to/dataset.csv
```

## Example

Using the Titanic `train.csv` dataset:

```text
==================================================
                DATASET ANALYZER
==================================================

==================================================
                DATASET OVERVIEW
==================================================
File       : data/train.csv
Rows       : 891
Columns    : 12

==================================================
                    COLUMNS
==================================================
 1. PassengerId
 2. Survived
 3. Pclass
 4. Name
 5. Sex
 6. Age
 7. SibSp
 8. Parch
 9. Ticket
10. Fare
11. Cabin
12. Embarked

==================================================
               MISSING VALUES
==================================================
  Column  Missing  Percentage
     Age      177      19.87%
   Cabin      687      77.10%
Embarked        2       0.22%
```

## Error Handling

The CLI validates the input before analyzing the dataset.

### File not found

```bash
python dataset_analyzer.py data/not-found.csv
```

Output:

```text
Error: File not found: data/not-found.csv
```

### Unsupported file type

```bash
python dataset_analyzer.py data/example.txt
```

Output:

```text
Error: Only CSV files are supported.
```

## Dataset

The project was initially tested using the **Titanic dataset**.

The dataset contains information about passengers, including:

- Passenger ID
- Survival status
- Passenger class
- Name
- Sex
- Age
- Number of siblings/spouses
- Number of parents/children
- Ticket
- Fare
- Cabin
- Port of embarkation

The dataset is useful for this project because it contains both numerical and categorical data, as well as missing values.

## Learning Objectives

This project was built to practice the fundamentals of Python data analysis and CLI application development.

### Python

- Functions
- Function arguments and return values
- Modules and imports
- Exception handling
- Command-line arguments
- Basic input validation

### Pandas

- Reading CSV files
- DataFrames
- Dataset dimensions
- Column selection
- Data types
- Missing-value analysis
- Descriptive statistics
- Duplicate detection
- Numerical and categorical column selection

### NumPy

- Numerical data type selection
- Working with Pandas and NumPy together

### CLI Development

- Using `argparse`
- Accepting file paths from the terminal
- Validating user input
- Handling expected errors
- Generating readable terminal output

## Architecture

The application follows a simple pipeline:

```text
User
 │
 │ CSV file path
 ▼
CLI
 │
 │ argparse
 ▼
File Validation
 │
 ▼
CSV Loader
 │
 │ Pandas
 ▼
DataFrame
 │
 ├── Dataset Overview
 ├── Column Information
 ├── Schema
 ├── Missing Values
 ├── Numerical Statistics
 ├── Duplicate Detection
 └── Column Categories
 │
 ▼
Terminal Report
```

## Future Improvements

Possible future improvements include:

- Add categorical value-frequency analysis
- Add outlier detection
- Add data-quality scoring
- Add Matplotlib visualizations
- Add Seaborn statistical visualizations
- Generate correlation heatmaps
- Export reports to files
- Support additional dataset formats
- Add automated tests
- Package the application as an installable CLI tool

## Status

**Completed — v1**

The current version provides the core CSV analysis functionality and a command-line interface.

## Part of My AI Engineering Journey

This project is part of my broader **AI Engineering** learning roadmap.

The progression will move from:

```text
Python & Data Analysis
        ↓
Machine Learning
        ↓
Deep Learning
        ↓
NLP
        ↓
Generative AI
        ↓
RAG
        ↓
AI Agents
        ↓
Computer Vision
        ↓
Speech AI
        ↓
MLOps & Deployment
        ↓
Production AI Systems
```

The Dataset Analyzer provides the foundation for understanding and profiling datasets before moving into machine learning and more advanced AI projects.
