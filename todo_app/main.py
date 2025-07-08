from warnings import catch_warnings

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo + '\n')
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
    elif user_action.startswith("show"):
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        for idx, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{idx + 1} - {item}")
    elif user_action.startswith("edit"):
        try:
            idx = int(user_action[5:])
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
            edit_todo = input("Enter new todo: ")
            todos[idx - 1] = edit_todo + '\n'
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid. Please try again.")
            continue
    elif user_action.startswith("complete"):
        idx = int(user_action[9:])
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        completed_todo = todos.pop(idx - 1)
        completed_todo = completed_todo.strip('\n')
        print(f"{completed_todo} is completed")
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Bye!")