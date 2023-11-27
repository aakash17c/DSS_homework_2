import random


def random_number(min, max):
    
    # Selecting Random integer with this function.
    
    return random.randint(min, max)


def choose_operator():
    # selecting operator to be used in calcution
    return random.choice(['+', '-', '*'])


def main_calculation(random_first_number, random_second_number, o):
    # funtion to make the main calculatin for the quiz
    p = f"{random_first_number} {o} {random_second_number}"
    if o == '+':a = random_first_number + random_second_number
    elif o == '-': a = random_first_number - random_second_number
    else: a = random_first_number * random_second_number
    return p, a

def math_quiz():
    score = 0 # initializing score to zero
    total_questions = 10 # assignig the value to variable total question.

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(1,total_questions):
        # using funtion to ger random number, by passing this values in the funtion named - randon_number
        random_first_number = random_number(1, 10); random_second_number = random_number(1, 5); o = choose_operator()

        # calling main_calculation funtion and assigning values to Answer and Problem variables
    
        PROBLEM, ANSWER = main_calculation(random_first_number, random_second_number, o)
        print("\nQuestion: ", {PROBLEM})
        useranswer = int(input("Your answer: "))
        # using if else case statements to calculate point if user answers correclty or print if "Wrong answer" if answer is wrong
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
# Final code

