import random

computer_point = 0
user_point = 0


def stone_paper_scissor():

    print("\nINSTRUCTION\n\nPress 'st' for Stone\nPress 'pa' for Paper\nPress 'sc' for Scissor")

    
    def computer_win():
        print("\nComputer Win ! You Lose")
        print(f"Your input is {user_input}. Computer input is {computer_input}")
        global computer_point                  # Function doesnot allow to change the gloabal variable with out permission
        computer_point += 1

    def user_win():
        print("\nYou Win")
        print(f"Your input is {user_input}. Computer input is {computer_input}")
        global user_point
        user_point += 1
    n = 1
    while n <= 5:
        game_keys = ["Stone", "Paper", "Scissor"]
        computer_input = random.choice(game_keys)
        user_shortcut_input = input("\nEnter your choice = ")

        # Checking and convert user inputp

        if user_shortcut_input == "st":
            user_input = "Stone"
        elif user_shortcut_input == "pa":
            user_input = "Paper"
        elif user_shortcut_input == "sc":
            user_input = "Scissor"
        elif user_shortcut_input == "exit":
            break
        else:
            print("Wrong Input. Please giv correct input")
            continue

        if user_input == computer_input:
            print("\nDraw")
            print(f"Your input is {user_input}. Computer input is {computer_input}")
            print(f"\nChance left {5 - n}")
            n += 1
            continue

        # For user input Stone


        if user_input == "Stone":

            if computer_input == "Paper":
                computer_win()
            else:
                user_win()
            print(f"\nChance left {5 - n}")
            n += 1
            
        # For user input Paper


        elif user_input == "Paper":

            if computer_input == "Scissor":
                computer_win()

            else:
                user_win()
            print(f"\nChance left {5 - n}")
            n += 1

        # For user input Scissor


        elif user_input == "Scissor":

            if computer_input == "Stone":
                computer_win()
            else:
                user_win()
            print(f"\nChance left {5 - n}")
            n += 1


    print(f"\nYour point = {user_point}")
    print(f"Computer point = {computer_point}")

    if user_point > computer_point:
        print("\nYou win the match")
    elif user_point < computer_point:
        print("Computer win the match")
    else:
        print("Match Draw")

    play_again_input = input("Do you want to play again?\n\nPress 'y' for 'YES' and 'press any key' for 'NO' = ")

    if play_again_input == "y":
        stone_paper_scissor()
    else:
        print("Thank You for Playing")

stone_paper_scissor()