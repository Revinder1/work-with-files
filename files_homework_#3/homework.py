# Если выполнить код, создастся файл Result_file.txt с требуемой информацией

file_name1 = '1.txt'
file_name2 = '2.txt'
file_name3 = '3.txt'


def file_read(file):
    with open(file, 'r', encoding='utf-8') as new:
        return new.read()


with open(file_name1, 'r', encoding='utf-8') as file1:
    with open(file_name2, 'r', encoding='utf-8') as file2:
        with open(file_name3, 'r', encoding='utf-8') as file3:
            new_dict = dict()
            new_dict[file_name1] = len(file1.readlines())
            new_dict[file_name2] = len(file2.readlines())
            new_dict[file_name3] = len(file3.readlines())
            sorted_dict = dict()
            sorted_keys = sorted(new_dict, key=new_dict.get)
            for i in sorted_keys:
                sorted_dict[i] = new_dict[i]


with open(file_name1, 'r', encoding='utf-8') as file1:
    with open(file_name2, 'r', encoding='utf-8') as file2:
        with open(file_name3, 'r', encoding='utf-8') as file3:
            with open('Result_file.txt', 'a+', encoding='utf-8') as new_file:
                for keys, values in sorted_dict.items():
                    string = f'{keys}\n{values}\n{file_read(keys).strip()}\n'
                    new_file.write(string)
