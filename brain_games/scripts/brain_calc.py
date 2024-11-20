import random, prompt
from brain_games.cli import generate_num, welcome_user



def check_answer():
    attempts = 3
    while attempts!=0:
        num =  generate_num()
        num2 = generate_num()
        operations="+-*"
        operation = operations[random.randint(0, len(operations) - 1)]
        result = int(eval(f'{num}{operation}{num2}'))
        print (f'{num} {operation} {num2}?')
        answer = eval(prompt.string("Your answer:"))
        
        if answer == result:
            print ("correct!")
            attempts-=1
            if attempts==0:print(f"Congratulations!")
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was '{result}'.")
            print (f"Let`s try again ")
            break


def main():
    print ("What is the result of the expression?")
    check_answer()
