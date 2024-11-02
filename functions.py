FILEPATH = "todos.txt"

def read_todoList(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items."""
    with open(filepath, 'r') as file_local:
        todoList_local = file_local.readlines()
    return todoList_local

def write_todoList(todoList_arg, filepath=FILEPATH):
    """ Write a to-do item in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todoList_arg)