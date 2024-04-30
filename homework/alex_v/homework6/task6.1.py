text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

split_words = text.split()
print(split_words)

for word in split_words:
    special_signs = ''
    if word[-1] in [',', '.']:
        special_signs = split_words[-1]
        word = word[:-1]
    result = [word + 'ing' + special_signs]
    new_text = ''.join(result)

    print(new_text)
