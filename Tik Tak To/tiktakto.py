import time

border_show = f"""
      1 |  2  | 3
    ----|-----|----
      4 |  5  | 6
    ----|-----|----
      7 |  8  | 9
"""






print(border_show)
print("This is the game board, please choose a number from 1-9 to place your X or O in the corresponding position.\n\t\tThe game board will be updated after each turn.\n","-"*100)
# print(game_show)

a,b,c,d,e,f,g,h,i = "","","","","","","","",""

switch_player = 0


def player1():
    time.sleep(0.2)
    global a,b,c,d,e,f,g,h,i
    player1_input = input("Player 1: ").lower().strip()

    if player1_input not in ["1","2","3","4","5","6","7","8","9"]:
      print("Invalid input. Please choose a number from 1-9.")
      player1()

    # Create a temporary mapping for the current board state to easily check the chosen position
    board_state = {
        "1": a,
        "2": b,
        "3": c,
        "4": d,
        "5": e,
        "6": f,
        "7": g,
        "8": h,
        "9": i
    }

    if board_state[player1_input] in ["X", "O"]:
        print("This position is already taken. Please choose another position.")
        player1()

    if   player1_input == "1": a = "X"
    elif player1_input == "2": b = "X"
    elif player1_input == "3": c = "X"
    elif player1_input == "4": d = "X"
    elif player1_input == "5": e = "X"
    elif player1_input == "6": f = "X"
    elif player1_input == "7": g = "X"
    elif player1_input == "8": h = "X"
    elif player1_input == "9": i = "X"

    game_show = f"""
    {a:>2}  | {b:>2}  | {c}
    ----|-----|----
    {d:>2}  | {e:>2}  | {f}
    ----|-----|----
    {g:>2}  | {h:>2}  | {i}
              """
    print(game_show)

def player2():
    time.sleep(0.2)
    global a,b,c,d,e,f,g,h,i
    player2_input = input("Player 2: ").lower().strip()

    if player2_input not in ["1","2","3","4","5","6","7","8","9"]:
      print("Invalid input. Please choose a number from 1-9.")
      player2()

    board_state = {
        "1": a,
        "2": b,
        "3": c,
        "4": d,
        "5": e,
        "6": f,
        "7": g,
        "8": h,
        "9": i
    }

    if board_state[player2_input] in ["X", "O"]:
        print("This position is already taken. Please choose another position.")
        player2()
    
    if   player2_input == "1": a = "O"
    elif player2_input == "2": b = "O"
    elif player2_input == "3": c = "O"
    elif player2_input == "4": d = "O"
    elif player2_input == "5": e = "O"
    elif player2_input == "6": f = "O"
    elif player2_input == "7": g = "O"
    elif player2_input == "8": h = "O"
    elif player2_input == "9": i = "O"

    game_show = f"""
    {a:>2}  | {b:>2}  | {c}
    ----|-----|----
    {d:>2}  | {e:>2}  | {f}
    ----|-----|----
    {g:>2}  | {h:>2}  | {i}
              """
    print(game_show)

def check_winner():
    global a,b,c,d,e,f,g,h,i

    if (a == b == c != "") or (d == e == f != "") or (g == h == i != "") or \
       (a == d == g != "") or (b == e == h != "") or (c == f == i != "") or \
       (a == e == i != "") or (c == e == g != ""):
        return True
    else:
        return False



while True:
  if switch_player == 0:
      player1()
      if check_winner():
          print("Player 1 wins!")
          break
      switch_player = 1
  else:
      player2()
      if check_winner():
          print("Player 2 wins!")
          break
      switch_player = 0
