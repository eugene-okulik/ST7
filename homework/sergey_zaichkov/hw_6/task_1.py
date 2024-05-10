phrase = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
          "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
result = ""

# Version 1
for word in phrase.split():
    if word.endswith(','):
        result += word[:-1] + 'ing, '
    elif word.endswith('.'):
        result += word[:-1] + 'ing. '
    else:
        result += word + 'ing '
print(result)


# # Version 2
# for word in phrase.split():
#     index = word.find(',') if ',' in word else word.find('.') if '.' in word else None
#     if index:
#         result += word[:index] + 'ing' + word[index:] + ' '
#     else:
#         result += word + 'ing '
# print(result)


# # Version 3
# for word in phrase.split():
#     (index := word.find(',')) != -1 or (index := word.find('.'))
#     if index != -1:
#         result += word[:index] + 'ing' + word[index:] + ' '
#     else:
#         result += word + 'ing '
# print(result)
