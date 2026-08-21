import random 
import sys

def starting():
    level = input("\t(Easy) (Normal) (Hard)\nChoose here: ")

    random_num_easy = random.randint(1,20)
    random_num_normal = random.randint(1,50)
    random_num_hard = random.randint(1,100)

    def easy(n):
        while True:
            try:
                guessing = int(input("\nGuess the number: "))
            except:
                print("-"*100,"\nPlease use just numbers!\n"+"-"*100)
                return easy(n)
            
            if guessing < n:
                print("Higher")
            elif guessing > n:
                print("Lower")
            else:
                print("You got it")
                exit()


    def normal(n):
        try:
            guessing = int(input("\nGuess the number: "))
        except:
            print("-"*100,"\nPlease use just numbers!\n"+"-"*100)
            return normal(n)
        
        if guessing < n:
            print("Higher")
        elif guessing > n:
            print("Lower")
        else:
            print("You got it")
            exit()


    def hard(n):
        while True:
            try:
                guessing = int(input("\nGuess the number: "))
            except:
                print("-"*100,"\nPlease use just numbers!\n"+"-"*100)
                return hard(n)
            
            if guessing < n:
                print("Higher")
            elif guessing > n:
                print("Lower")
            else:
                print("You got it")
                exit()
        
        
    if level.lower() == 'easy':
        while True:
            easy(random_num_easy)
    elif level.lower() == 'normal':
        while True:
            normal(random_num_normal)
    elif level.lower() == 'hard':
        while True:
            hard(random_num_hard)
    else:
        print("-"*100,"\nPlease choose a level\n"+"-"*100)
        return starting()

starting()