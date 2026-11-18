import random

questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "A": "function",
        "B": "def",
        "C": "define",
        "D": "fun",
        "answer": "B"
    },
    {
        "question": "Which data type stores multiple items in an ordered collection?",
        "A": "Integer",
        "B": "String",
        "C": "List",
        "D": "Boolean",
        "answer": "C"
    },
    {
        "question": "Which loop is commonly used to iterate over a sequence?",
        "A": "if",
        "B": "for",
        "C": "def",
        "D": "try",
        "answer": "B"
    }
]

random.shuffle(questions)

score = 0

for question in questions:
    print("\n" + question["question"])

    print("A.", question["A"])
    print("B.", question["B"])
    print("C.", question["C"])
    print("D.", question["D"])

    while True:
        try:
            answer = input("Enter your answer (A/B/C/D):").upper().strip()

            if answer not in ["A", "B", "C", "D"]:
                raise ValueError("Please enter A, B, C or D")
            break

        except ValueError as error:
            print(error)

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
        print("Correct answer:", question["answer"])

total_questions = len(questions)
percentage = (score / total_questions) * 100

print("\nQUIZ RESULTS")
print("Your score:", score, "/", total_questions)
print("Percentage:", round(percentage, 2), "%")

if percentage >= 80:
    print("Excellent! You did very well")
elif percentage >= 50:
    print("Good! Keep practising")
else:
    print("Try again! Review the concepts and attempt again")