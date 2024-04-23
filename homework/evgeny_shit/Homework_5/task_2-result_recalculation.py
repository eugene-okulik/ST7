str1 = 'результат операции: 42'
str2 = 'результат операции: 514'
str3 = 'результат работы программы: 9'

num1 = int(str1[str1.find(":") + 2:])
num2 = int(str2[str2.find(":") + 2:])
num3 = int(str3[str3.find(":") + 2:])

result1 = num1 + 10
result2 = num2 + 10
result3 = num3 + 10

print(result1, result2, result3)
