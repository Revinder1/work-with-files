import os

directory = os.getcwd()
data = dict()
files = os.listdir(directory)

for file in files:
    if file.endswith('.txt'):
        with open(file, 'r', encoding='utf-8') as x:
            text = x.readlines()
            data[file] = text

sorted_list = sorted(data.items(), key=lambda i: len(i[1]))

with open('result.txt', 'a', encoding='utf-8') as file:
    for i in sorted_list:
        file.write(i[0] + '\n')
        file.write(str(len(i[1])) + '\n')
        file.write(' '.join(i[1]) + '\n')
