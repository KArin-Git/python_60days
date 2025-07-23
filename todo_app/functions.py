# Module
def get_todos(filepath='files/todos.txt'):
    """
    Read a text file
    :param filepath:
    :return: a list of todos items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
if __name__ == "__main__":
    print(help(get_todos))  # Print doc string of the function when executed directly
def write_todos(todos_arg, filepath='files/todos.txt'):
    """ Write the todos items list in the text file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)