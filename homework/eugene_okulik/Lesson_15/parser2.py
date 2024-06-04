with open('options.txt', encoding='utf-8') as data_file:
    data = data_file.read()


features = {}

blocks = data.split('\n\n')

# print(blocks)


for block in blocks:
    content = block.splitlines()
    # key, value = content[0], content[1:]
    key, *value = content
    features[key] = value

print(features)
