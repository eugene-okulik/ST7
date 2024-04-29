
line_1 = 'результат операции: 42'
line_2 = 'результат операции: 514'
line_3 = 'результат работы программы: 9'


list_1 = line_1.split()
list_2 = line_2.split()
list_3 = line_3.split()

number_1 = int(list_1[-1])
total_1 = number_1 + 10
print(total_1)

number_2 = int(list_2[-1])
total_2 = number_2 + 10
print(total_2)

number_3 = int(list_3[-1])
total_3 = number_3 + 10
print(total_3)
