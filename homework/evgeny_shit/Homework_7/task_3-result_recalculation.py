def recalc(s):
    number = int(s[s.find(":") + 2:])
    return number + 10


str1 = 'результат операции: 42'
str2 = 'результат операции: 54'
str3 = 'результат работы программы: 209'
str4 = 'результат: 2'

for i in str1, str2, str3, str4:
    print(f'{recalc(i)} - result of recalculating "{i}" row')
