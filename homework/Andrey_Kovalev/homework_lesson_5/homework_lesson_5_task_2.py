results = [
    "результат операции: 42",
    "результат операции: 514",
    "результат работы программы: 9"
]

for result in results:
    colon_index = result.index(':') + 2
    number_str = result[colon_index:]

    print("Результат работы программы + 10:", int(number_str) + 10)
