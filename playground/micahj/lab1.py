import os
import json

cur_dir = os.path.dirname(os.path.abspath(__file__))
print('cur_dir', cur_dir)

playground_dir = os.path.split(cur_dir)[0]
print('playground_dir', playground_dir)

print(os.path.abspath(__file__))
print(os.path.realpath(__file__))
print(os.path.relpath(__file__))


def read_file(file_path):
    with open(file_path) as f:
        return f.read()


def read_file_lines(file_path):
    with open(file_path) as f:
        return f.readlines()


def reader(file_path):
    with open(file_path) as f:
        counter = 0
        for line in f:
            yield counter, line
            counter += 1


def text_sandwich(text, char='-', spacer_count=25):
    spacer = char * max(spacer_count, len(text))
    return f'\n{spacer}\n{text}\n{spacer}'


# a berry file
file_path = os.path.join(playground_dir, 'berry', 'lab1', 'README.txt')

print(text_sandwich('reading whole file content'))
content = read_file(file_path)
print(content)

print(text_sandwich('using a generator to loop (with a fakey enumerate)'))
for line_number, line in reader(file_path):
    print(line_number, line)

print(text_sandwich('reading file as a list of lines'))
print(json.dumps(read_file_lines(file_path), indent=3))