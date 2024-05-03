words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for key, value in words.items():
    for x in range(value):
        print(key * value)
