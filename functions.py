FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items"""
    # Dessa forma não é necessário fechar o arquivo com .close()
    with open(filepath, "r") as file_local:
            todos_local = file_local.readlines()
            
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Abrindo o arquivo todos.txt em modo de gravação e inserindo o novo valor da variável "todos" nele."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
