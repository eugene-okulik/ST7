import datetime

input_data = "Jan 15, 2023 - 12:05:33"
data = datetime.datetime.strptime(input_data, "%b %d, %Y - %H:%M:%S")
print(data.strftime("%B"))
print(data.strftime("%d.%m.%Y, %H:%M"))
