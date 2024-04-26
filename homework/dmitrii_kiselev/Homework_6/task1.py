string = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'.split()

for i in range(len(string)):
    if string[i][-1] == ',':
        string[i] = string[i][:-1] + 'ing,'
    elif string[i][-1] == '.':
        string[i] = string[i][:-1] + 'ing.'
    else:
        string[i] += 'ing'

print(' '.join(string))
