text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')
list_from_text = text.split()
print(list_from_text)
new_list = []
for world in list_from_text:
    if world.endswith(','):
        new_list.append(world[:-1] + 'ing' + ',')
    elif world.endswith('.'):
        new_list.append(world[:-1] + 'ing' + '.')
    else:
        new_list.append(world + 'ing')
print(new_list)
updated_text = ' '.join(new_list)
print(updated_text)
