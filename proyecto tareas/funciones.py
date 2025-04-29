def get_todos(filepath="todos.txt"):
    """Read a textfile and
    return the list of to-do items
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("hello")
    print(get_todos())