# import os
from pathlib import Path


def get_uppercase(text):
    return ''.join(char for char in text if char.isupper())


def read_file(filepath):
    try:
        with filepath.open('r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None


def main():
    base_dir = Path(__file__).resolve().parent.parent.parent
    filepath = base_dir / 'eugene_okulik' / 'hw_13' / 'data.txt'

    content = read_file(filepath)
    if content is not None:
        uppercase_letters = get_uppercase(content)
        print(uppercase_letters)


if __name__ == "__main__":
    main()

# def read_and_print_uppercase(filepath):
#     try:
#         with open(filepath, 'r') as file:
#             content = file.read()
#             uppercase_letters = ''.join([char for char in content if char.isupper()])
#             print(uppercase_letters)
#     except FileNotFoundError:
#         print(f"File on path {filepath} not found.")
#     except Exception as e:
#         print(f"An error has occurred: {e}")
#
# if __name__ == "__main__":
#     base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#     filepath = os.path.join(base_dir, 'eugene_okulik', 'hw_13', 'data.txt')
#     read_and_print_uppercase(filepath)
