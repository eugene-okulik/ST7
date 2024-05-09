text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        + 'dignissim vitae libero')
split_words = text.split()
words_list = []

for word in split_words:
    if word.endswith(',') or word.endswith('.'):
        specials = word[-1]
        word = word[:-1]
    else:
        specials = ''

    transformed_word = word + 'ing' + specials
    words_list.append(transformed_word)

transformed_text = ' '.join(words_list)

print(transformed_text)
