import time
import random

"""
Math Quiz Game

A simple console-based math quiz game built with Python.

Features:
- 10 random math questions
- 10-second time limit
- Random arithmetic operators
- Final score summary
- Input validation

Created by Ma3ih-dev
"""

def show_welcome(): # Display the welcome screen and start the game countdown.
       
    print("""
=========================================
       🎉 WELCOME TO MATH QUIZ 🎉
=========================================

📚 Rules:

• You will answer 10 random math questions.
• You have 10 seconds to answer each question.
• ✔️ Correct answer: +1 point
• ✘ Wrong answer: No point awarded.
• ⏰ If time runs out, the game moves to the next question.

Good luck and have fun!

=========================================
""")

    while True:
        start = input("Press ENTER to start the game...")

        if start == "":
            break

        print("❌ Invalid input! Just press ENTER to start.\n")

    print("\nStarting in...\n")

    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    print("""
=========================================
          🚀 GAME STARTED! 🚀
=========================================
""")
    time.sleep(1)


def generate_question(): # Generate a random math question and return the question and its answer.

    operators = ["+", "-", "*", "/"]
    operator = random.choice(operators)

    if operator == "/":
        divisor = random.randint(2, 10)
        answer = random.randint(2, 10)
        dividend = divisor * answer

        question = f"{dividend} {operator} {divisor} = ?"

    else:
        num1 = random.randint(2, 100)
        num2 = random.randint(2, 100)

        if operator == "-":
            if num2 > num1:
                num1, num2 = num2, num1

        question = f"{num1} {operator} {num2} = ?"

        if operator == "+":
            answer = num1 + num2
        elif operator == "-":
            answer = num1 - num2
        else:
            answer = num1 * num2

    return question, answer
         
     
def play_game(): # Run the main game loop and return the player's score.

    question_count = 1
    score = 0
    wrong_answer = 0

    for _ in range(10):

        question, answer = generate_question()

        print("=" * 40)
        print(f"Question {question_count}/10")
        print("=" * 40)
        print(question)

        start_time = time.time()

        try:
            user_answer = int(input("\nEnter your answer: "))
        except ValueError:
            print("\n❌ Invalid input! Please enter a number.")
            wrong_answer += 1
            question_count += 1
            continue

        end_time = time.time()

        if end_time - start_time > 10:
            print("\n⏰ Time is up!")
            print(f"The correct answer was: {answer}")
            wrong_answer += 1

        elif user_answer == answer:
            score += 1
            print("\n✅ Correct!")

        else:
            wrong_answer += 1
            print("\n❌ Wrong answer!")
            print(f"Correct answer: {answer}")

        question_count += 1
        print()

    return score, wrong_answer
    


def show_result(score, wrong_answer): # Display the final game results and performance message.

    print("\n" + "=" * 40)
    print("           🏆 GAME OVER 🏆")
    print("=" * 40)

    print(f"✅ Correct Answers : {score}")
    print(f"❌ Wrong Answers   : {wrong_answer}")

    print("-" * 40)

    if score == 10:
        print("🌟 Outstanding! Perfect score!")

    elif score >= 8:
        print("🎉 Excellent job! You did great!")

    elif score >= 5:
        print("👍 Good work! Keep practicing!")

    else:
        print("📚 Don't give up! Practice makes perfect!")

    print("=" * 40)
    print("Thanks for playing Math Quiz! ❤️")
    print("Created by Ma3ihdev")
    print("=" * 40)
    

def main(): # Start the Math Quiz game.

    show_welcome()

    score, wrong_answer = play_game()

    show_result(score, wrong_answer)


if __name__ == "__main__":
    main()





    
    




     

    

