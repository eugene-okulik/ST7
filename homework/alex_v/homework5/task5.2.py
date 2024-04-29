operation_one = "результат операции: 42"
operation_two = "результат операции: 514"
operation_three = "результат операции: 9"

result1 = int(operation_one.split(': ')[-1]) + 10
result2 = int(operation_two.split(': ')[-1]) + 10
result3 = int(operation_three.split(': ')[-1]) + 10

print(result1)
print(result2)
print(result3)
