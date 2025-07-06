password = input("Please enter your password: ")
result = []
# length greater or equal to 8
if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

# contain at least 1 digit
digit = False
# contain at least 1 capital character
upper = False
for character in password:
    if character.isdigit():
        digit = True
    if character.isupper():
        upper = True
result.append(digit)
result.append(upper)

print(result)
print(all(result)) # capture False if has

if all(result):
    print("Strong Password")
else:
    print("Weak Password")