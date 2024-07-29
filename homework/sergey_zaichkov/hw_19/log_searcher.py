import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("folder", help="Path to folder")
parser.add_argument("text", help="Text to search")
args = parser.parse_args()


class LogSearcher:
    def __init__(self, path_dir: str, text: str):
        self.__path_dir = path_dir
        self.__text = text
        self.__files = self.__list_dir()

    def __list_dir(self) -> str:
        for file in os.listdir(self.__path_dir):
            if os.path.isfile(os.path.join(self.__path_dir, file)):
                if file.split('.')[-1] == 'log':
                    yield file

    def __read_file(self, file: str) -> str:
        with open(os.path.join(self.__path_dir, file)) as f:
            for line in f:
                yield line

    def search_text(self) -> None:
        for file in self.__files:
            print(f"File {file}:")
            for i, line in enumerate(self.__read_file(file), start=1):
                if self.__text in line:
                    word_index = line.find(self.__text)
                    words_before = line[:word_index].strip().split(' ')[-5:]
                    words_after = line[word_index + len(self.__text):].strip().split(' ')[:5]
                    result = f"{' '.join(words_before)} {self.__text} {' '.join(words_after)}"
                    print(f"Str#{i}: {result}")
            print("--------------------------------------------------------------")


if __name__ == "__main__":
    log_searcher = LogSearcher(path_dir=args.folder, text=args.text)
    log_searcher.search_text()
