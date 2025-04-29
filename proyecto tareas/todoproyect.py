import modulos.funciones
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is",now)

while True:
    usuario = input("type add, show, complete, edit or exit: ")
    usuario = usuario.strip()


    if usuario.startswith("add"):
        todo = usuario[4:]

        todos = modulos.funciones.get_todos()

        todos.append(todo+'\n')

        funciones.write_todos(todos)


    elif usuario.startswith("show"):
        todos =  funciones.get_todos()

        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}.-{item}"
            print(row)


    elif usuario.startswith("edit"):
        try:

            nume = int(usuario[5:])
            print(nume)
            nume = nume - 1


            todos = funciones.get_todos()

            new_todo = input("Enter new todo: ")
            todos[nume] = new_todo + '\n'

            funciones.write_todos(todos)

        except ValueError:
            print("your commmand is not valid.")
            continue


    elif usuario.startswith("complete"):
        try:
            numero = int(usuario[9:])

            todos =  funciones.get_todos()
            index = numero -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            funciones.write_todos(todos)

            message = f"el todo {todo_to_remove} fue removido de la lista"
            print(message)
        except IndexError:
            print("there is no item with that number.")
            continue



    elif usuario.startswith("exit"):
        break

    else:
        print("comand is not valid")



print("bye cabrones")



