quotes = [
    "Be yourself; everyone else is already taken. – Oscar Wilde",
    "In the middle of difficulty lies opportunity. – Albert Einstein",
    "The only thing we have to fear is fear itself. – Franklin D. Roosevelt",
    "I think, therefore I am. – René Descartes",
    "Stay hungry, stay foolish. – Steve Jobs"
]

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for quote, filename in zip(quotes, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(quote)
    file.close()