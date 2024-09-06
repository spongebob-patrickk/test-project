import random
def generate_word()->str:
    #glkajgvlk;agh
    mylist=["paper","scissors","rock"]
    return random.choice(mylist)
def user__prompt()->str:
    return input("pleasse enter your word\n")
def is_equal(system_word:str,user_word:str):
    return system_word==user_word
def game_loop(system_word=generate_word(),cycle=3):
    while cycle>0:
        user_value=user__prompt
        if is_equal(system_word=user_value):
            print("you win")
            exit()
        cycle-=1
    print("you loose")
    game_loop()
