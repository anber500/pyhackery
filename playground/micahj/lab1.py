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


def findfiles(condition, startin):
    """
    condition is a lambda taking a file name condition
    """
    results = []
    for d, _, files in os.walk(startin):
        results.extend([os.path.join(d, f) for f in files if condition(f)])
    return results


# a berry file
berry_file_path = os.path.join(playground_dir, 'berry', 'lab1', 'README.txt')

# reading whole file content
print(text_sandwich('reading whole file content'))
content = read_file(berry_file_path)
print(content)

# using a generator to loop (with a fakey enumerate)
print(text_sandwich('using a generator to loop (with a fakey enumerate)'))
for line_number, line in reader(berry_file_path):
    print(line_number, line)

# reading file as a list of lines
print(text_sandwich('reading file as a list of lines'))
print(json.dumps(read_file_lines(berry_file_path), indent=3))

# show filtering the lines with list comprehension
lines = read_file_lines(berry_file_path)
filtered = [line for line in lines if 'porn' in line]
print(text_sandwich("berry porn"))
print(json.dumps(filtered, indent=2))

# show filtering the lines with list comprehension - lines reversed
filtered = [''.join(reversed(line)) for line in lines if 'porn' in line]
print(text_sandwich("backwards berry porn"))
print(json.dumps(filtered, indent=2))

# ujse os walk to locate files in a directory tree
files = findfiles(lambda f: '.py' in f.lower(), startin=playground_dir)
print(text_sandwich('find files with os walk'))
print(json.dumps(files, indent=3))
