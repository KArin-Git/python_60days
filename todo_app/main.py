user_prompt = "Enter a todo: "
todos = []
while True:
    todo = input(user_prompt)
    print("User input is: " + todo.capitalize())
    todos.append(todo)
    print(todos)