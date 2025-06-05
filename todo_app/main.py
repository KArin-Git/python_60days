todos = []
while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            idx = int(input("Number of the todo to edit: "))
            edit_todo = todos[idx - 1]
            print("The todo that you want to edit is " + edit_todo)
            todos[idx - 1] = input("Enter new todo: ")
            print(todos)
        case "exit":
            break

print("Bye!")