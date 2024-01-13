FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Read a text file
    and return the list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items in a text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


"""when you run this file __name__ will become __main__
but when you are invoking this file from another python file 
then __name__ will become functions i.e the name of this file"""
if __name__ == "__main__":
    print("Hello this is the file content below:")
    print(get_todos())
