from art import logo, vs
from game_data import data 
import random 

def format_data(account):
    """format the account data into printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """use if statement to check if user is correct"""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b' 

#display art 
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

#keep going until flag is 0
while game_should_continue:
    #generate a random account from the game data
    account_a = account_b 
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data) 

    print(f'Item A: {format_data(account_a)}.')
    print(vs)
    print(f'Item B: {format_data(account_b)}.')

    #ask user for a guess
    guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    #check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct: 
        score += 1
        print(f"\nYou're right! Current score: {score}.\n")
    else:
        game_should_continue = False 
        print(f"\nSorry, that's wrong. Final score: {score}\n")

