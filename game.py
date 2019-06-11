# game.py
def determine_winner(user_choice, computer_choice):
       """
       Determines the winning choice between two choices from selectable options: "rock", "paper", or "scissors".
       Returns the winning choice (e.g. "paper"), or None if there is a tie.
       Example: determine_winner("rock", "paper")
       """
       
    if user_choice == computer_choice:
        winner = None # the outcome is a tie
    else:
        choices = [user_choice, computer_choice]
        choices.sort() # FYI: this is mutating
        if choices == ["paper", "rock"]:
            winner = "paper"
        elif choices == ["paper", "scissors"]:
            winner = "scissors"
        elif choices == ["rock", "scissors"]:
            winner = "rock"
        else:
            raise ValueError("OOPS, SOMETHING WENT WRONG")
            
    return winner

if __name__ == "__main__":

    print("Rock, Paper, Scissors, Shoot!")

    print("------------------------")
    print("Welcome to my Rock-Paper-Scissors game...")
    print("------------------------")


    options = ["rock", "paper", "scissors"]

    user_choice = input ("Please choose either 'rock', 'paper', or 'scissors': ")

    if user_choice in options:
        print("You chose: ", user_choice)
    else:
        print("Expecting one of: 'rock', 'paper', or 'scissors' (lower case). Please try again.")
        exit()


    import random

    def random_choice(options=["rock", "paper", "scissors"]):
        return random.choice(options)


    random.shuffle(options)
    computer_choice = random.choice(options)

    print("The computer chose:", computer_choice)
    print("------------------------")


    

    winner_choice = determine_winner(user_choice, computer_choice)


    if winner_choice:
        if winner_choice == user_choice:
            print("Congratulations, you won!")
        elif winner_choice == computer_choice:
            print("Oh, the computer won. It's ok.")

    else:
        print("Oh, it's a tie.")

    print("------------------------")
    print("Thanks for playing. Please play again!")