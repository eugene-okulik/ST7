import random


def message():
    function_list = ['результат операции: 42', 'результат операции: 514', 'результат работы программы: 9']
    return random.choice(function_list)


return_message = message()

print(int(return_message[return_message.find(': ') + 2:]) + 10)
