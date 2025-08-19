# obj can be stored in var
name = 'John'
last_name = 'Smith'
id = '10221'
members = 5
height = 1.75

# obj can be produced by func
name = input('What is your age?')
print(name) # 'Arin'

height = input('What is your height?')
print(height) # '155'
float(height) # 155.0

# methods that return an output
groceries = ['vinegar', 'olives', 'bread']
variable = groceries.append('apples')
print(groceries) # ['vinegar', 'olives', 'bread', 'apples]

groceries.sort()
print(groceries) # ['apples', 'bread', 'olives', 'vinegar']

# list of methods
dir(str)
dir(list)

help(str.upper)