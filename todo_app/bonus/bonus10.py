try:
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    if width == length:
        exit("The rectangle isn't square.")
    area = width * length
    print(f"The area of the rectangle is: {area}")
except ValueError:
    print("Enter the number value")