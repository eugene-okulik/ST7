import json


class CountryData:
    def __init__(self, filename):
        self.__filename = filename
        self.__data = self.__read_file()
        self.__country = self.__data['Country']
        self.__avg_temp = self.__data['avg_temp']
        self._is_hot = True if self.__avg_temp >= 30 else False

    @property
    def data(self):
        return self.__data

    def __read_file(self):
        file_data = open(self.__filename)
        data = json.load(file_data)
        return data


data1 = CountryData('data1.txt')

print(data1.data)
print(data1._is_hot)
