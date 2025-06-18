new_member = input("Enter a member name: ") + '\n'
file = open('../files/members.txt', 'r')
content = file.readlines()
file.close()
content.append(new_member)
file = open('../files/members.txt', 'w')
file.writelines(content)
file.close()

for name in content:
    print(f"{name}")