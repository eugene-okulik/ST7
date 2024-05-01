
text_1 = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel.'
'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)

list_text_1 = text_1.split()
for words in list_text_1:
    if words.endswith(','):
        print(words[:-1] + 'ing' + ',')
    elif words.endswith('.'):
        print(words[:-1] + 'ing' + '.')
    else:
        print(words)
