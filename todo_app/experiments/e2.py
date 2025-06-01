# Exp1: Infinite Loop
# while True:
#     print("Infinite loop")

# Exp2: put var declare in while loop > bad practice to declare str:user_prompt multiple times as unnecessary
todos = []
while True:
    user_prompt = "Enter a todo: "
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)

# Exp3: str.title()
user_prompt = "Enter a todo: "
todos = []
while True:
    todo = input(user_prompt)
    print(todo.title())
    todos.append(todo)

# Exp4: msg for method without ()
user_prompt = "Enter a todo: "
todos = []
while True:
    todo = input(user_prompt)
    print(todo.title) # throw <built-in method title of str object at 0x104c3fbf0>
    todos.append(todo)



