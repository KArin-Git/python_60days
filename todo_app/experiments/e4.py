todos = ['Todo1', 'Todo2', 'Todo3']

for idx, todo in enumerate(todos):
    print(f"{idx + 1}-{todo}")

print(f"The last todo is {len(todos)}-{todo}. This sentence is printed outside for-loop")