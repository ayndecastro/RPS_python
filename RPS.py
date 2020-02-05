import random

rps = ("Rock", "Paper", "Scissors")


class Score:  # score tracking
    def __init__(self):
        self.total = 0

    def win(self):
        self.total += 1


def player_choice():  # player input choice

    while True:
        x = input("Rock Paper Scissors: ")
        # track the first letter and lowercase it. incase player miss spells or messes up the caps we still get an input
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


# use score class to score for both pc and player score tracking
pc_score = Score()
player_score = Score()

# we use a while loop to constantly re-initiate rps
while True:

    player = player_choice()
    # pc choice is chosen in random from the rps tuple using indexing with random module
    pc = rps[random.randrange(0, 3)]

    # game logic
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

    # if pc scores 5 then player loses. It prompts a question if player wants to play again or not.
    if pc_score.total == 5:
        print("YOU LOSE")
        if input("Would you like to play again? yes or no ")[0].lower() == 'y':
            # if player wants to play again, then we have to reset the score
            player_score.total = 0
            pc_score.total = 0
            continue
        else:
            # if not, then we break the while loop
            print("Thank you for playing")
            break

    # if player scores 5 then pc loses. It prompts a question if player wants to play again or not.
    if player_score.total == 5:
        print("YOU WIN!")
        if input("Would you like to play again? yes or no ")[0].lower() == 'y':
            # if player wants to play again, then we have to reset the score
            player_score.total = 0
            pc_score.total = 0
            continue
        else:
            # if not, then we break the while loop
            print("Thank you for playing")
            break
