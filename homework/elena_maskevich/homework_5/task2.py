first_line = 'результат операции: 42'
second_line = 'результат операции: 514'
third_line = 'результат работы программы: 9'
first_index = first_line.find(':')
second_index = first_line.index(':')
third_index = third_line.find(':')
print(first_index)
first_number = int(first_line[(first_index + 2):]) + 10
second_number = int(second_line[(second_index + 2):]) + 10
third_number = int(third_line[(third_index + 2):]) + 10

print(first_number + second_number + third_number)
