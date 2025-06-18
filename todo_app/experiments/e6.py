# Create Multiple file
filenames = ['a.txt', 'b.txt', 'c.txt']
for filename in filenames:
    file = open(f"../files/{filename}", 'w')
    name = filename.replace('.txt', '')
    file.write(f"Hello World!\n"
               f"I am {name.title()}!\n")
    file.close()

# Reading Multiple Files
for filename in filenames:
    file = open(f"../files/{filename}", 'r')
    content = file.read()
    file.close()
    print(content)


