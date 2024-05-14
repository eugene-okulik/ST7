result1 = "результат операции: 42"
result2 = "результат операции: 54"
result3 = "результат работы программы: 209"
result4 = "результат: 2"


def add_ten(*input_strings):
    for string in input_strings:
        print(int(string.split()[-1]) + 10)


add_ten(result1, result2, result3, result4)
