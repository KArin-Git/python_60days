todos = ['Todo1', 'Todo2', 'Todo3']

for idx, todo in enumerate(todos):
    print(f"{idx + 1}-{todo}")

print(f"The last todo is {len(todos)}-{todo}. This sentence is printed outside for-loop")


for i, j in enumerate("Hello"):
    print(i, j)
# 0 H
# 1 e
# 2 l
# 3 l
# 4 o

a = enumerate(['a', 'b', 'c'])
print(a) # <enumerate object at 0x104921670>
print(list(a)) # [(0, 'a'), (1, 'b'), (2, 'c')] -> this is list of tuple

for i, item in [(0, 'a'), (1, 'b'), (2, 'c')]:
    print(i, item)
# 0 a
# 1 b
# 2 c