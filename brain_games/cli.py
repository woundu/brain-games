import prompt , random


MIN =1
MAX = 99

def generate_num():
    return random.randint(MIN,MAX)

def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name?')
    print(f"Hello,{name}!")
    return name

def play():
    attempts =3


