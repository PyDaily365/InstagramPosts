import random
def math_quiz():
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    # Randomly choose an operation (addition or subtraction)
    operation = random.choice(['+', '-'])
    # Calculate correct answer
    if operation == '+':
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2
    # Ask the question and get user's answer
    try:
        user_answer = int(input(f"What is {num1}{operation}{num2}? "))
        # Check if answer is correct
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Sorry. The answer is {correct_answer}.")
    except ValueError:
        print(f"Please enter a valid number!")
if __name__ == "__main__":
    math_quiz()
# Learn: create a +/- math game using random numbers