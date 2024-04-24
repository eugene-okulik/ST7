def recalculate(s):
    number = int(s[s.find(":") + 2:])
    return number + 10


str1 = 'результат операции: 42'
str2 = 'результат операции: 514'
str3 = 'результат работы программы: 9'

result1 = recalculate(str1)
result2 = recalculate(str2)
result3 = recalculate(str3)

print(result1, result2, result3)
