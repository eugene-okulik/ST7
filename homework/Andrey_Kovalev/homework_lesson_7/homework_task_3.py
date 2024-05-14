result_strings = ["результат операции: 42", "результат операции: 54", "результат работы программы: 209",
                  "результат: 2"
                  ]

operation_results = [int(result.split(': ')[-1]) + 10 for result in result_strings]
print(operation_results)
