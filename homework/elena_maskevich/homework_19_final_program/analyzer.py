# нужно сделать программу, которая сможет:
# - ожидать от пользователя, что при запуске программы он укажет полный путь к папке, в которой лежат файлы с логами
# - ожидать от пользователя, что он укажет какой текст нужно найти в файлах
# - находить строки, в которых встречается тот текст, который пользователь попросил найти
# - выводить на экран результат своей работы в котором будет казано название файла, где найден текст и порядковый номер
# строки файла, в которой был найден текст
# - выводить на экран кусок той строки, в которой был найден текст

import argparse
import os

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
# root1 = os.path.dirname(__file__)
# print(root1)
# roo11_path = os.path.join(root1, 'analyzer.py')
# print(roo11_path)
task_path = os.path.join(project_root, 'homework', 'eugene_okulik', 'data', 'logs')
parser = argparse.ArgumentParser()
parser.add_argument('task_path', help='путь к директории с логами')
parser.add_argument('word_for_search', help='слово для поиска')
args = parser.parse_args()

entries = os.listdir(task_path)
for entry in entries:
    file_path = os.path.join(task_path, entry)
    with open(file_path) as logs_file:
        data = logs_file.read()
        data_array = data.split('\n')
        indices = []
        count = 0
        for elem in range(len(data_array)):
            if args.word_for_search in data_array[elem]:
                count += 1
                indices.append(elem)
        if len(indices) > 0:
            print(f'Путь к файлу - {file_path}', end='\n')

        for element in indices:
            text_array = str(data_array[element]).split()
            text_string = str(text_array)
            c = text_string.find(args.word_for_search)
            word_index = text_array.index(args.word_for_search)
            for i in range(word_index - 4, word_index + 6):
                if i >= 0:
                    print(text_array[i])
        print(f'Номера строк, где встречается искомое слово - {indices}', end='\n\n')
