password = input("Please enter your password: ")
result = {}
# length greater or equal to 8
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

# contain at least 1 digit
digit = False
# contain at least 1 capital character
upper = False
for character in password:
    if character.isdigit():
        digit = True
    if character.isupper():
        upper = True
result["digit"] = digit
result["upper"] = upper

print(result)
print(all(result.values()))

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")