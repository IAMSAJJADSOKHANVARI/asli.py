def get_todos(filepath='files/text_file.txt'):
    """ Read a textfile and return the list of
     to_do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='files/text_file.txt'):
    """ Write the to-do item list in the text file.  """

    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print(__name__)
if __name__ == "__main__":
    print("Hello from function! ")
    print(get_todos())
