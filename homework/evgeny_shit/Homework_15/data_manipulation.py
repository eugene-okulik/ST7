from pathlib import Path
from datetime import datetime, timedelta


def read_file(filepath):
    try:
        with filepath.open('r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None


def process_date(date_str, action):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

    match action:
        case action if "на неделю позже" in action:
            new_date = date_obj + timedelta(weeks=1)
            return f"{date_str} -> {new_date}"

        case action if "день недели" in action:
            day_of_week = date_obj.strftime("%A")
            return f"{date_str} -> {day_of_week}"

        case action if "сколько дней назад" in action:
            today = datetime.now()
            days_diff = (today - date_obj).days
            return f"{date_str} -> {days_diff} days ago"

        case _:
            return None


def process_dates(content):
    results = []
    for line in content:
        parts = line.split(' - ')
        if len(parts) != 2:
            continue
        date_str = parts[0].strip().split('. ')[-1]
        action = parts[1].strip()

        result = process_date(date_str, action)
        if result:
            results.append(result)

    return results


def main():
    base_dir = Path(__file__).resolve().parent.parent.parent
    filepath = base_dir / 'eugene_okulik' / 'hw_15' / 'data.txt'

    content = read_file(filepath)
    if content:
        results = process_dates(content)
        for result in results:
            print(result)


if __name__ == "__main__":
    main()
