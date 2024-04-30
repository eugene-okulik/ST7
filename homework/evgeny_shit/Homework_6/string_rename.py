def add_ing(word):
    if word[-1] in [",", "."]:
        return word[:-1] + 'ing' + word[-1]
    return word + 'ing'


text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        + 'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

words = text.split()
words_ing = []

for word in words:
    words_ing.append(add_ing(word))

text_with_ing = " ".join(words_ing)

print(text_with_ing)
