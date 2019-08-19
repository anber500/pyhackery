"""This utility will generate Results according to the settings in Options file"""
import os
from datetime import date

def write_results(email_result_entry, destination_path, file_name, file_extension):
    destination_file_path = os.path.join(destination_path, os.path.join(
        file_name + date.today().strftime('%Y%m%d') + file_extension))

    with open(destination_file_path, 'w') as file:
        file.write(email_result_entry)

