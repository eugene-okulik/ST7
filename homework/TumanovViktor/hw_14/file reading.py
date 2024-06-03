import os

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
file_path = os.path.join(project_root, 'homework', 'eugene_okulik', 'hw_13')
eugene_okulik = os.path.join(file_path, 'data.txt')


with open(eugene_okulik, encoding='utf-8') as my_file:
    for i in my_file:
        for char in i:
            if char.isupper():
                print(char, end='')


# with open('D:/Python/projectTumanov/ST7/homework/kate_hushcha/my_test_file.txt', 'r', encoding='utf-8') as kate_file:
#    reading = kate_file.read()
#    print(reading)
