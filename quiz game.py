def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if answer == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}")
    print(f"\n🎉 You got {score} out of {len(questions)} correct!")

if __name__ == "__main__":
    quiz_questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Berlin", "D. Rome"],
            "answer": "A"
        },
        {
            "question": "Which language is used for web apps?",
            "options": ["A. Python", "B. Java", "C. PHP", "D. All of the above"],
            "answer": "D"
        },
        {
            "question": "What does CPU stand for?",
            "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Central Processor Utility"],
            "answer": "B"
        },
        {
            "question": "Who developed Python?",
            "options": ["A. Dennis Ritchie", "B. Bjarne Stroustrup", "C. James Gosling", "D. Guido van Rossum"],
            "answer": "D"
        }
    ]
    
    print("🎓 Welcome to the Quiz Game!")
    run_quiz(quiz_questions)
