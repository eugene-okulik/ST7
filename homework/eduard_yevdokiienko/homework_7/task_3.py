result_1 = 'результат операции: 42'
result_2 = 'результат операции: 54'
result_3 = 'результат работы программы: 209'
result_4 = 'результат: 2'


def calc(results):
    index = results.index(':') + 2
    numb = int(results[index:]) + 10
    print(numb)


for x in [result_1, result_2, result_3, result_4]:
    calc(x)
