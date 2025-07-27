import json

with open("questions.json", "r") as file:
    # load as str
    content = file.read()

# load as list or dict depend on the data that store in json
data = json.loads(content)
# iterate over dictionary
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index + 1} - {alternative}")
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

# summary answer
score = 0
for idx, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score += 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    msg = f"{result} for Question Number: {idx + 1} \n" \
          f"Your answer: {question['user_choice']}, "\
          f"Correct Answer: {question['correct_answer']} \n"
    print(msg)
print(f"{score} / {len(data)}")


