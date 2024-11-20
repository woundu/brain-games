import random, prompt
from brain_games.cli import generate_num

attempts = 3

def check(answer,num):
    even = num % 2 ==0 
    odd = num % 2 !=0
    if answer=="yes" and even or answer=="no" and odd:
        result = True
    return result

def generate_question():
    while attempts!=0:
        num =  generate_num()
        print (f"Question: {num}?")
        answer = prompt.string("Your answer:")
        result =  check(answer, num)
        if result:
            print ("Correct!")
            attempts-=1
            if attempts==0:
                print("Congratulations")
        else:
            print ("You loose!")
           
def main():

    print ("Answer \'yes\' if the number is even, otherwise answer \'no\'.")
    generate_question()
    


    
    
