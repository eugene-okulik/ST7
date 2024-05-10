text = ("Etiam tincidunt neque erat, "
        "quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
words = text.split()
modified_words = []

for word in words:
    punctuation = ''
    if word[-1] in ',.':
        punctuation = word[-1]
        word = word[:-1]

    modified_words.append(word + 'ing' + punctuation)

modified_text = ' '.join(modified_words)
print(modified_text)
