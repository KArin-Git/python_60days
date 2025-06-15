while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            # open file and read
            file = open('todos.txt', 'r')
            # store value from file in todos list
            todos = file.readlines()
            # append a new todo list
            todos.append(todo)
            # open file for overwrite
            file = open('todos.txt', 'w')
            # overwrite
            file.writelines(todos)
        case "show":
            for idx, item in enumerate(todos):
                print(f"{idx + 1}: {item}")
        case "edit":
            idx = int(input("Number of the todo to edit: "))
            edit_todo = todos[idx - 1]
            print("The todo that you want to edit is " + edit_todo)
            todos[idx - 1] = input("Enter new todo: ")
            print(todos)
        case "complete":
            idx = int(input("Number of the todo to complete: "))
            # print(f"{idx}: {todos[idx - 1]} was removed")
            completed_todo = todos.pop(idx - 1)
            print(f"{completed_todo} is completed")
        case "exit":
            break

print("Bye!")