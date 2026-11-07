# Student Scores Project

A small Python project based on a previous programming coursework assignment.

## Features

- Generate student score data in CSV format.
- Read student scores from a CSV file.
- Calculate the highest score, lowest score, and average score.

## Requirements

- Python 3.14.4 (tested)
- No third-party Python packages required

## Setup

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on Linux / WSL:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

The requirements file is currently empty because the project only uses Python standard library modules.

## Usage

Run the statistics program:

```bash
python main.py
```

Regenerate the sample CSV data:

```bash
python generate_data.py
```

**Note:** Running `generate_data.py` overwrites `data/student.csv`.

## Project Structure

```text
student_scores_project/
├── data/
│   └── student.csv
├── generate_data.py
├── main.py
├── requirements.txt
└── .gitignore
```

## Sample Output

```text
python最高分： 95
python最低分： 75
python平均分： 85.62
```

