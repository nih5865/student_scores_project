import csv
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent / "data" / "student.csv"


def load_scores(csv_path):
    score_list = []

    with open(csv_path, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            score_list.append(int(row[3]))

    return score_list


def calculate_statistics(scores):
    max_s = max(scores)
    min_s = min(scores)
    avg_s = sum(scores) / len(scores)

    return max_s, min_s, avg_s


def main():
    scores = load_scores(CSV_PATH)

    max_s, min_s, avg_s = calculate_statistics(scores)

    print("python最高分：", max_s)
    print("python最低分：", min_s)
    print("python平均分：", round(avg_s, 2))


if __name__ == "__main__":
    main()