# Importing packages
import json
import requests


# Read TO DO Items
def read_first_todo():
    with requests.get('https://jsonplaceholder.typicode.com/todos/') as response:
        if response.status_code == 200:
            print("API status : Success")
            output = response.json()

            #Lab 2 - Task 1 Print item one by one
            for item in output:
                print_json_data(item)

            #Lab 2 - Task 2 List Comprehension
            print(" ")
            print_todos_for_first(output)

        else:
            print("API status : Failed")

# Print data
def print_json_data(jsonData):
    user_id = jsonData['userId']
    user_title = jsonData['title']
    user_completed = jsonData['completed']
    print(user_id,',',user_title,',',user_completed)

# Print TO DO items id = 1
def print_todos_for_first(responseData):
    filteredData = [item for item in responseData if item['userId'] == 1]

    print('These are in the first set')
    print('==========================')

    for new_item in filteredData:
        print_json_data(new_item)