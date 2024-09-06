import random
maximum=10
def generate_num()->int:
    return random.randint(1,maximum)
def user_prompt()->int:
    return int(input("please enter your number\n"))
def is_equal(system_number:int,user_number:int):
    return system_number==user_number
def game_loop(system_number=generate_num(),cycle=3):
    while cycle>0:
        user_value=user_prompt()
        if is_equal(system_number,user_value):
            print("you win")
            exit()
        cycle-=1
    print("you loose")
game_loop()