import random 

symbols = ["+", "-", "*", "/"]

print("\n\tPlease choose a symbol...")
print("\t","'+'", "'-'", "'*'", "'/'", "'all'", "\n")

random_symbol = random.choice(symbols)


    
a, b = 0, 0


count = 1
correct_counter = 0
wrong_counter = 0



def Starting():
    try:
        global level, attempt, start,num1, num2, a, b 

        start = input("Symbol: ").lower()
        level = input("\nEnter a level (Example: (E) for easy, (N) for normal, (H) for hard\nEnter: ").lower()
        attempt = int(input("How many questions do want to try?: "))

        if level == "e": a, b = 1, 10
        elif level == "n": a, b = 5, 15
        elif level == "h": a, b = 13, 25

        num1 = random.randint(a, b)
        num2 = random.randint(a, b)

    except ValueError or NameError:
        print("\nPlease Fill The Inputs Correctlly !\n") 


def ALL():
    try:
        global num1, num2, symbols, level, attempt, count, correct_counter, wrong_counter, random_symbol, a, b 


        if random_symbol == "/" and num1 < num2:
                num1,num2 = num2,num1 

        show_question = f"""
            Answer Below
      /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾/
     /{num1:>7} {random_symbol:>2} {num2:>2}      /
    /___________________/
    """
        print(show_question)

        answer = float(input("Answer: "))
        result = 0
        

        if random_symbol == "+": result = num1 + num2 
        elif random_symbol == "-": result = num1 - num2 
        elif random_symbol == "*": result = num1 * num2 
        elif random_symbol == "/": result = round(num1 / num2, 2)

        if answer == result:
            correct_counter = correct_counter + 1
            print(f"\nCorrect!\n{count} of {attempt}\nCorrect Answers: {correct_counter:>3}\nWrong   Answers : {wrong_counter:>3}")
            count = count + 1
            random_symbol = random.choice(symbols)
            num1 = random.randint(a, b)
            num2 = random.randint(a, b)
        else:
            wrong_counter = wrong_counter + 1
            print(f"Wrong!\n{count} of {attempt}\nCorrect Answers: {correct_counter:>3}\nWrong  Answers:  {wrong_counter:>3}")
            num1 = random.randint(a, b)
            num2 = random.randint(a, b)
            count = count + 1

    except ValueError:
         print("\n __________________________\n| To  answer, use numbers |\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
         print("             /\\\n"+"            /  \\\n"+"           / !? \\\n","          ‾‾‾‾‾‾")
         return ALL()


def Minus():
    try:
        global num1, num2, level, attempt, count, correct_counter, wrong_counter, a, b 

        symbol = "-"

        show_question = f"""
                Answer Below
          /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾/
         /{num1:>7} {symbol:>2} {num2:>2}      /
        /___________________/
        """

        print(show_question)

        result = num1 - num2 

        answer = int(input("Answer: "))

        if answer == result:
            correct_counter = correct_counter + 1
            print(f"\nCorrect!\n{count} of {attempt}\nCorrect Answers: {correct_counter:>3}\nWrong   Answers : {wrong_counter:>3}")
            num1 = random.randint(a, b)
            num2 = random.randint(a, b)
            count = count + 1
        else:
            wrong_counter = wrong_counter + 1
            print(f"\nWrong!\n{count} of {attempt}\nCorrect Answers: {correct_counter:>3}\nWrong  Answers:  {wrong_counter:>3}")
            num1 = random.randint(a, b)
            num2 = random.randint(a, b)
            count = count + 1

    except ValueError:
        print("\n __________________________\n| To  answer, use numbers |\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print("             /\\\n"+"            /  \\\n"+"           / !? \\\n","          ‾‾‾‾‾‾")
        return Minus()



def Plus():
    try:
        global num1, num2, level, attempt, count, correct_counter, wrong_counter, question_change, a, b 

        symbol = "+"

        show_question = f"""
                Answer Below
          /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾/
         /{num1:>7} {symbol:>2} {num2:>2}      /
        /___________________/
        """

        print(show_question)

        result = num1 + num2 

        answer = int(input("Answer: "))

        if answer == result:
            correct_counter = correct_counter + 1
            print(f"\nCorrect!\n{count} of {attempt}\nCorrect Answers: {correct_counter:>3}\nWrong Answers: {wrong_counter:>3}")
            num1 = random.randint(a, b)
            num2 = random.randint(a, b)
            count = count + 1
        else:
            wrong_counter = wrong_counter + 1
            print(f"\nWrong!\n{count} of {attempt}\nCorrect Answers: {correct_counter:>3}\nWrong  Answers:  {wrong_counter:>3}")
            num1 = random.randint(a, b)
            num2 = random.randint(a, b)
            count = count + 1

    except ValueError:
        print("\n __________________________\n| To  answer, use numbers |\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print("             /\\\n"+"            /  \\\n"+"           / !? \\\n","          ‾‾‾‾‾‾")
        return Plus()





def Moltiply():
    try:
        global num1, num2, level, attempt, count, correct_counter, wrong_counter, a, b 

        symbol = "*"

        show_question = f"""
                Answer Below
          /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾/
         /{num1:>7} {symbol:>2} {num2:>2}      /
        /___________________/
        """

        print(show_question)

        result = num1 * num2 

        answer = int(input("Answer: "))

        if answer == result:
            correct_counter = correct_counter + 1
            print(f"\nCorrect!\n{count} of {attempt}\nCorrect Answers: {correct_counter:>3}\nWrong   Answers : {wrong_counter:>3}")
            num1 = random.randint(a, b)
            num2 = random.randint(a, b)
            count = count + 1

        else:
            wrong_counter = wrong_counter + 1
            print(f"\nWrong!\n{count} of {attempt}\nCorrect Answers: {correct_counter:>3}\nWrong  Answers:  {wrong_counter:>3}")
            num1 = random.randint(a, b)
            num2 = random.randint(a, b)
            count = count + 1

    except ValueError:
        print("\n __________________________\n| To  answer, use numbers |\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print("             /\\\n"+"            /  \\\n"+"           / !? \\\n","          ‾‾‾‾‾‾")
        return Moltiply()



def Devition():
    try:
        global num1, num2, level, attempt, count, correct_counter, wrong_counter, a, b 

        symbol = "/"

        if num1 < num2:
            num1,num2 = num2,num1 

        show_question = f"""
                Answer Below
          /‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾/
         /{num1:>7} {symbol:>2} {num2:>2}      /
        /___________________/
        """

        print(show_question)

        result = num1 / num2 

        answer = int(input("Answer: "))

        if answer == result:
            correct_counter = correct_counter + 1
            print(f"\nCorrect!\n{count} of {attempt}\nCorrect Answers: {correct_counter:>3}\nWrong   Answers : {wrong_counter:>3}")
            num1 = random.randint(a, b)
            num2 = random.randint(a, b)
            count = count + 1

        else:
            wrong_counter = wrong_counter + 1
            print(f"\nWrong!\n{count} of {attempt}\nCorrect Answers: {correct_counter:>3}\nWrong  Answers:  {wrong_counter:>3}")
            num1 = random.randint(a, b)
            num2 = random.randint(a, b)
            count = count + 1

    except ValueError:
        print("\n __________________________\n| To  answer, use numbers |\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print("             /\\\n"+"            /  \\\n"+"           / !? \\\n","          ‾‾‾‾‾‾")
        return Devition()

    
while True:
    if a == 0 and b == 0: Starting()

    if count == attempt + 1:
        break 

    if start == "-": Minus()
    elif start == "+": Plus()
    elif start == "*": Moltiply()
    elif start == "/": Devition()
    elif start == "all": ALL()