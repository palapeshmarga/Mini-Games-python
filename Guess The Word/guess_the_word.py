import os
import random 

with open(os.path.join(os.path.dirname(__file__), 'words.txt'), 'r') as file:
    words = [line.strip() for line in file.readlines()]

word = random.choice(words).upper()

a,b,c,d = '?', '?', '?', '?'

attempt = 0

def check():
    global a,b,c,d
    global attempt

    result = f"""
    _________________________
    |     |     |     |     |
    |  {a}  |  {b}  |  {c}  |  {d}  |
    |     |     |     |     |
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
"""
    print(result)

    print("Type 'hint' to get a hint.")
    guess = input("Guess the word: ").strip().upper()
    attempt += 1

    if guess == 'HINT':
        nums = []

        if a == '?':nums.append(0)
        else:
            if 0 in nums:nums.remove(0)
        if b == '?':nums.append(1)
        else:
            if 1 in nums:nums.remove(1)
        if c == '?':nums.append(2)
        else:
            if 2 in nums:nums.remove(2)
        if d == '?':nums.append(3)
        else:
            if 3 in nums:nums.remove(3)

                    
        random_index = random.choice(nums)
        # nums.remove(random_index)
        # print(nums, random_index)

        match random_index:
            case 0:a = word[0]
            case 1:b = word[1]
            case 2:c = word[2]
            case 3:d = word[3]
        return

        


    if len(guess) != 4:
        print('It should be 4 letters long\nPlase try again')
        return
    
    if guess[0] == word[0]:a = guess[0]
    if guess[1] == word[1]:b = guess[1]
    if guess[2] == word[2]:c = guess[2]
    if guess[3] == word[3]:d = guess[3]

    if a == word[0] and b == word[1] and c == word[2] and d == word[3]:
        print(result)
        print(f"\n\n Congratulations! You guessed the word! 🎉️\n    You have guessed it with ({attempt}) attempts.")

while True:
    check()
    if a == word[0] and b == word[1] and c == word[2] and d == word[3]:
        result = f"""
    _________________________
    |     |     |     |     |
    |  {a}  |  {b}  |  {c}  |  {d}  |
    |     |     |     |     |
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
"""
        print(result)
        break