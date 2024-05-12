questions = [
    {
        "prompt": "What is the United States Capitol?",
        "options": ["A. Austin", "B. New York", "C. Los Angles", "D. Washington D.C"],
        "answer": "D"
    },
    {
        "prompt": "How many countries are in North America",
        "options": ["A. 4", "B. 3", "C. 9", "D. 2"],
        "answer": "B"
    },
    {
        "prompt": "What is the largest state in the USA",
        "options": ["A. Texas", "B. California", "C. Alaska", "D. Florida"],
        "answer": "C"
    },
    {
        "prompt": "Who is the CEO of Tesla?",
        "options": ["A. Elon Musk", "B. Jeff Bezos", "C. Mark Zuckerburg"],
        "answer": "A"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print (question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer: (A, B, C, D): ").upper()
        if answer == question["answer"]:
            print("Correct, good job! \n")
            score += 1
        else:
            print("Incorrect! The correct anwswer was",  question["answer"], "\n")

    print(f"You got {score} out of {len(questions)} questions correct.")


run_quiz(questions)