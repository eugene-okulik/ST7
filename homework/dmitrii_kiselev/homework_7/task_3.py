def result(string):
    return int(string.split(' ')[-1]) + 10


for strin in ['результат операции: 42', 'результат операции: 54', 'результат работы программы: 209', 'результат: 2']:
    print(result(strin))
