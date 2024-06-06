from pathlib import Path
from datetime import datetime, timedelta


def read_file_content(file_path):
    with file_path.open('r', encoding='utf-8') as file:
        return file.readlines()


def modify_date(date_string, specified_action):
    date_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f")

    if "на неделю позже" in specified_action:
        new_date = date_object + timedelta(weeks=1)
        return f"{date_string} -> {new_date}"

    elif "день недели" in specified_action:
        weekday = date_object.strftime("%A")
        return f"{date_string} -> {weekday}"

    elif "сколько дней назад" in specified_action:
        current_date = datetime.now()
        days_difference = (current_date - date_object).days
        return f"{date_string} -> {days_difference} дней назад"

    else:
        return None


def process_all_dates(file_content):
    processed_results = []
    for line in file_content:
        parts = line.split(' - ')
        if len(parts) != 2:
            continue
        date_string = parts[0].strip().split('. ')[-1]
        specified_action = parts[1].strip()

        processed_result = modify_date(date_string, specified_action)
        if processed_result:
            processed_results.append(processed_result)

    return processed_results


base_directory = Path(__file__).resolve().parent.parent.parent
data_file_path = base_directory / 'eugene_okulik' / 'hw_15' / 'data.txt'


file_content = read_file_content(data_file_path)
if file_content:
    processed_results = process_all_dates(file_content)
    for result in processed_results:
        print(result)
