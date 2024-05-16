temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

filtered_list = list(filter(lambda x: x > 28, temperatures))

max_temp = max(filtered_list)
min_temp = min(filtered_list)
average_temp = round(sum(filtered_list) / len(filtered_list))

print(f'Maximum temp is {max_temp} degrees')
print(f'Minimum temp is {min_temp} degrees')
print(f'Average temp is {average_temp} degrees')
