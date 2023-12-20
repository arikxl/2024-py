import random


def play():
    user = input("🪨  , 📃  , or ✂️  ? ")
    computer = random.choice(["🪨" ,"📃 ","✂️"])

    if user == computer:
        return 'DRAW!'

    if check_win(user, computer):
        return 'You Won!'
    
    return 'You Lost!'


def check_win(user, comp):
    if (user == '✂️' and comp == '📃') or  (user == '🪨' and comp == '✂️') or( user == '📃' and comp == '') :
        return True


print(play())
