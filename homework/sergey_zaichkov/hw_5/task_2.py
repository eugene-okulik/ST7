st1 = "результат операции: 42"
st2 = "результат операции: 514"
st3 = "результат работы программы: 9"

result1 = int(st1[st1.find(': ') + 2:]) + 10
result2 = int(st2[st2.find(': ') + 2:]) + 10
result3 = int(st3[st3.find(': ') + 2:]) + 10
print(result1)
print(result2)
print(result3)
