import random


rps = ("Rock", "Paper", "Scissors")


class Score:
    def __init__(self):
        self.total = 0

    def win(self):
        self.total += 1


def player_choice():

    while True:
        x = input("Rock Paper Scissors: ")

        if x[0].lower() == 'r':
            return "Rock"
        elif x[0].lower() == 'p':
            return "Paper"
        elif x[0].lower() == 's':
            return "Scissors"
        else:
            print("Sorry, try again")
            continue
        break


pc_score = Score()
player_score = Score()
while True:

    player = player_choice()
    pc = rps[random.randrange(0, 3)]

    if player == "Rock" and pc == "Scissors":
        player_score.win()
        print(f'''
        {player}
        {pc}

        Player score: {player_score.total}
        PC score: {pc_score.total}
        ''')
    elif player == "Scissors" and pc == "Paper":
        player_score.win()
        print(f'''
        {player}
        {pc}

        Player score: {player_score.total}
        PC score: {pc_score.total}
        ''')
    elif player == "Paper" and pc == "Rock":
        player_score.win()
        print(f'''
        {player}
        {pc}

        Player score: {player_score.total}
        PC score: {pc_score.total}
        ''')
    elif pc == "Rock" and player == "Scissors":
        pc_score.win()
        print(f'''
        {player}
        {pc}

        Player score: {player_score.total}
        PC score: {pc_score.total}
        ''')
    elif pc == "Scissors" and player == "Paper":
        pc_score.win()
        print(f'''
        {player}
        {pc}

        Player score: {player_score.total}
        PC score: {pc_score.total}
        ''')
    elif pc == "Paper" and player == "Rock":
        pc_score.win()
        print(f'''
        {player}
        {pc}

        Player score: {player_score.total}
        PC score: {pc_score.total}
        ''')
    else:
        print("draw")
        print(f'''
        {player}
        {pc}

        Player score: {player_score.total}
        PC score: {pc_score.total}
        ''')

    if pc_score.total == 5:
        print("YOU LOSE")
        if input("Would you like to play again? yes or no ")[0].lower() == 'y':
            player_score.total = 0
            pc_score.total = 0
            continue
        else:
            print("Thank you for playing")
            break

    if player_score.total == 5:
        print("YOU WIN!")
        if input("Would you like to play again? yes or no ")[0].lower() == 'y':
            player_score.total = 0
            pc_score.total = 0
            continue
        else:
            print("Thank you for playing")
            break
