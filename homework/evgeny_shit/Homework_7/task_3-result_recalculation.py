def recalc(s):
    number = int(s[s.find(":") + 2:])
    return number + 10


str1 = 'результат операции: 42'
str2 = 'результат операции: 514'
str3 = 'результат работы программы: 9'

for i in str1, str2, str3:
    print(f'{recalc(i)} - result of recalculating "{i}" row')

