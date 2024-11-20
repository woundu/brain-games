import random, prompt
MIN =1
MAX = 99
def generate_num():
    return random.randint(MIN,MAX)
   



ATTEMPTS = 3
        

def check_answer():
    attempts = 3
    while attempts!=0:
        num =  generate_num()
        print (f"{num}?")
        answer = prompt.string("Your answer:")
        if answer =="yes" and num % 2 ==0 or answer =="no" and num % 2 !=0: 
            print ("correct!")
            attempts-=1
            if attempts==0:print("congratulations!")
        else: 
            print("you loose!")
            break

      
def main():

    print ("Answer \'yes\' if the number is even, otherwise answer \'no\'.")
    check_answer()


    
    
