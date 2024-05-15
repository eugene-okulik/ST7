result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'

print(result1.index(':'))
print(result2.index(':'))
print(result3.index(':'))

index_1 = result1.index(':') + 2
char_1 = int(result1[index_1:])
char_1 += 10
print(char_1)

index_2 = result2.index(':') + 2
char_2 = int(result2[index_2:])
char_2 += 10
print(char_2)

index_3 = result3.index(':') + 2
char_3 = int(result3[index_3:])
char_3 += 10
print(char_3)
