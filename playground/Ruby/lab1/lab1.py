import logging
import os
import json
import re

print("hello")

logging.info("Welcome to lab1")


def lab1():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    dir_to_read = os.path.split(cur_dir)[0]
    print('Starting Point: ',dir_to_read)
    loaded_files = findfiles(lambda f: '.txt' in f.lower(), file_location=dir_to_read)    
    for i in loaded_files:
        custom_file = os.path.split(i)[1]
        regex_filename = '^import.*'
        my_file = re.match(regex_filename, custom_file)
        if my_file:
            print(text_sandwich(custom_file))
            read_file(i)  

def text_sandwich(text, char='-', spacer_count=25):
    spacer = char * max(spacer_count, len(text))
    return f'\n\n{text}\n{spacer}'

def read_file(f):
    f = open(f, 'r')    
    if f.mode == 'r':
        contents = f.read( )
        print(contents)
        f.close( )

def findfiles(check_condition,file_location):
    list_files = []
    for dirs,_,files in os.walk(file_location):
        list_files.extend([os.path.join(dirs,f) for f in files if check_condition(f)])    
    return list_files

def main():
    lab1()


if __name__ == "__main__":
    main()