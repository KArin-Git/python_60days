while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    if 'add' in user_action:
        todo = user_action[4:]
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo)
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
    if 'show' in user_action:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        for idx, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{idx + 1} - {item}")
    if 'edit' in user_action:
        idx = int(input("Number of the todo to edit: "))
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        edit_todo = input("Enter new todo: ")
        todos[idx - 1] = edit_todo + '\n'
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
    if 'complete' in user_action:
        idx = int(input("Number of the todo to complete: "))
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        completed_todo = todos.pop(idx - 1)
        completed_todo = completed_todo.strip('\n')
        print(f"{completed_todo} is completed")
        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
    if 'exit' in user_action:
        break

print("Bye!")