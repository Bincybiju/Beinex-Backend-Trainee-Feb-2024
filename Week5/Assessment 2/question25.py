"""Quiz game in python
"""
def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    for question_data in questions:
        question = question_data[0]
        options = question_data[1]
        answer = question_data[2]

        print(question)
        for i, option in enumerate(options, 1):
            print(f" {chr(65 + i - 1)}. {option}")

        user_answer = input("Your answer (type A, B, C, or D): ").upper()

        if user_answer.isalpha() and user_answer in ["A", "B", "C", "D"]:
            user_answer = options[ord(user_answer) - ord("A")]
        else:
            print("Invalid input. Skipping question.")
            continue

        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {answer}")

    print(f"You got {score} out of {total_questions} questions correct.")

questions = [
    ("Who wrote 'Romeo and Juliet'?", ["Shakespeare", "Dickens", "Hemingway"], "Shakespeare"),
    ("What is the largest planet in our solar system?", ["Jupiter", "Saturn", "Neptune"], "Jupiter"),
    ("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Michelangelo", "Pablo Picasso"], "Leonardo da Vinci"),
    ("What is the powerhouse of the cell?", ["Mitochondria", "Nucleus", "Ribosome"], "Mitochondria"),
    ("Which continent is the largest by land area?", ["Asia", "Africa", "North America"], "Asia"),
]

run_quiz(questions)
