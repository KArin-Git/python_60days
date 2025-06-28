while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
            todos.append(todo)
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case "show":
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
            for idx, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{idx + 1} - {item}")
        case "edit":
            idx = int(input("Number of the todo to edit: "))
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
            edit_todo = input("Enter new todo: ")
            todos[idx - 1] = edit_todo + '\n'
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case "complete":
            idx = int(input("Number of the todo to complete: "))
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
            completed_todo = todos.pop(idx - 1)
            completed_todo = completed_todo.strip('\n')
            print(f"{completed_todo} is completed")
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case "exit":
            break

print("Bye!")