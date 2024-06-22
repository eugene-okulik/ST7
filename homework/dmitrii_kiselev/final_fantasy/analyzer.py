import os
import sys


def serch_by_raw(string, element_for_search, words_count=5, ignore_capitalize=True, final_list=None):
    if element_for_search == '':
        return None
    if ignore_capitalize and element_for_search.lower() in string.lower():
        el_index = string.lower().index(element_for_search.lower())
    elif element_for_search in string:
        el_index = string.index(element_for_search)
    else:
        return None
    until_the_element = string[:el_index].split()
    after_the_element = string[el_index + len(element_for_search):].split()
    showing_element = string[el_index:el_index + len(element_for_search)]

    if len(until_the_element) > words_count:
        until_the_element = until_the_element[-words_count:]

    if len(after_the_element) > words_count:
        short_after_the_element = after_the_element[:words_count]
    else:
        short_after_the_element = after_the_element

    if final_list:
        final_list.append(until_the_element + [f'"{showing_element}"'] + short_after_the_element)
    else:
        final_list = [until_the_element + [f'"{showing_element}"'] + short_after_the_element]

    new_string = ' '.join(after_the_element)
    if element_for_search.lower() in new_string.lower():
        serch_by_raw(new_string, element_for_search, words_count, ignore_capitalize, final_list)
    return final_list


def search_in_file(file_path, element_for_search, words_count=5, ignore_capitalize=True):

    with open(file_path, 'r', encoding='utf-8') as my_file:
        count, final_dict = 0, {}
        while True:
            line = my_file.readline()
            if not line:
                break
            row_print = serch_by_raw(line, element_for_search, words_count, ignore_capitalize)
            if row_print:
                final_dict[count] = row_print
            count += 1

    return final_dict


def separate_files(dir_path, element_for_search, ignore_capitalize=True, words_count=5):
    files = os.listdir(dir_path)
    count = 0
    for file in files:
        files_dict = search_in_file(os.path.join(dir_path, file), element_for_search, words_count, ignore_capitalize)
        if files_dict:
            for key, value in files_dict.items():
                for funk_str in value:
                    funk_str = ' '.join(funk_str)
                    print(f'{count}. В файле {file} на строке {key} искомый элемент внутри: {funk_str}')
                    count += 1


def creating_arguments(params):
    if len(params) < 3:
        print('Недостаточно данных')
        params = [
            'analyzer.py', input('Введите корректный адрес папки с логами: '), input('Что хотите искать в логах: ')
        ]

    parametrs_tpl = (params[1],)
    if '--text' in params:
        parametrs_tpl += (params[params.index('--text') + 1],)
    else:
        parametrs_tpl += (params[2],)

    if '--ignore_capitalize' in params and params[params.index('--ignore_capitalize') + 1].title() == 'False':
        parametrs_tpl += (False,)

    if '--words_count' in params:
        parametrs_tpl += (int(params[params.index('--words_count') + 1]), )

    return parametrs_tpl


parametrs = sys.argv
separate_files(*creating_arguments(parametrs))
