def greet():
    msg = "hello"
    new_msg = msg.capitalize()
    print("Hey")
    return new_msg

def greet2():
    msg = "Hi"
    new_msg = msg.capitalize()

def greet3(msg):
    new_msg = msg.capitalize()
    return new_msg


greeting = greet()
print(greeting) # print new_msg which is Hello
print(greet2()) # print None
# print(len(greet2())) # TypeError
print(greet3("this is greet 3"))