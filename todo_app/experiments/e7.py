# with context manager without 2nd parameter >> auto assign 'r' >> help(open)
with open('../files/doc.txt') as file:
    print(file.read())
    content = file.read() # empty string as cursor move to the end in line 3
    print("Some text")

# file.read() >> ValueError: I/O operation on closed file. >> file.close() after finishing the with block
print(content)