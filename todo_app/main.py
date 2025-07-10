def get_todos(filepath='files/todos.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath='files/todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

# main
while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos)
    elif user_action.startswith("show"):
        todos = get_todos()
        for idx, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{idx + 1} - {item}")
    elif user_action.startswith("edit"):
        try:
            idx = int(user_action[5:])
            todos = get_todos()
            edit_todo = input("Enter new todo: ")
            todos[idx - 1] = edit_todo + '\n'
            write_todos(todos)
        except ValueError:
            print("Your command is not valid. Please try again.")
            continue
    elif user_action.startswith("complete"):
        try:
            idx = int(user_action[9:])
            todos = get_todos()
            completed_todo = todos.pop(idx - 1)
            completed_todo = completed_todo.strip('\n')
            print(f"{completed_todo} is completed")
            write_todos(todos)
        except IndexError:
            print("There is no item with that number. Please try again.")
            continue
    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Bye!")