txt = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
       'dignissim vitae libero')

st = txt.split()
new_text = []
for changes in st:
    if ',' in changes:
        changes = changes.replace(',', 'ing,')
    elif '.' in changes:
        changes = changes.replace('.', 'ing.')
    else:
        changes += 'ing'
    changes = changes + " "
    if changes != 0:
        new_text.append(changes)

string_text = ''.join(new_text)
print(string_text)
