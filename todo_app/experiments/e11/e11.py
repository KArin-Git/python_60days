import glob

my_file = glob.glob("files/*.txt")

for file_path in my_file:
    with open(file_path, "r") as file:
        print(file.read().upper())