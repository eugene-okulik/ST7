from datetime import datetime

date_str = "Jan 15, 2023 - 12:05:33"

date_obj = datetime.strptime(date_str, "%b %d, %Y - %H:%M:%S")

full_month_name = date_obj.strftime("%B")
print(f"Full month name: {full_month_name}")

formatted_date = date_obj.strftime("%d.%m.%Y, %H:%M")
print(f"Formatted date: {formatted_date}")
