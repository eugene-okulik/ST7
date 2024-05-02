
line_1 = 'результат операции: 42'
line_2 = 'результат операции: 514'
line_3 = 'результат работы программы: 9'

pos_1 = line_1.find(':')
sum_1 = pos_1+2
number_1 = int(line_1[sum_1:]) + 10
print(number_1)

pos_2 = line_2.find(':')
sum_2 = pos_2+2
number_2 = int(line_2[sum_2:]) + 10
print(number_2)

pos_3 = line_3.find(':')
sum_3 = pos_3+2
number_3 = int(line_3[sum_3:]) + 10
print(number_3)
