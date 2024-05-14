words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


# for key, value in words.items():
#    key *= value
#   print(key)

def result(words):
    for key, value in words.items():
        print(key * value)


print(result(words))
