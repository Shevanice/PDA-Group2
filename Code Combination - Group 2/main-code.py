#Main Menu

RESET = "\033[0m"
PURPLE = "\033[95m"
GRAY = "\033[90m"
WHITE = "\033[97m"
GREEN = "\033[92m"
RED = "\033[91m"

def main_menu():
    while True:
        print("\nWelcome to Group 2's presentation. This is the main menu section, "
              "which will be used to launch and play each game.")
              
        print(PURPLE +"-----------------------------------------------"+ RESET)
        print(PURPLE +"--------- Main Menu ----------")
        print("-----------------------------------------------"+ RESET)
  
        print( "Enter [M] To Play Maze Game"+ RESET)
        print("Enter [S] To Play Slot Machine"+ RESET)
        print("Enter [W] To Play Guess the number")
        print(RED +"Enter [E] To Exit"+ RESET)

        choice = input("\nSelect an option: ").strip().upper()

        match choice:
            case 'M':
                import maze_game
                maze_game.main()
            case 'S':
                import slot_machine
                game = slot_machine.slotMachine()
                while True:
                    print(PURPLE +"--------------------------------"+ RESET)
                    print(PURPLE +"==== Slot Machine Menu ===="+ RESET)
                    print(PURPLE +"--------------------------------"+ RESET)
                    print("Enter [P] to Play a Round")
                    print("Enter [D] to Deposit Money")
                    print("Enter [S] to Show Stats")
                    print("Enter [Q] to quit")
                    
                    sub_choice = input("Choose an option: ").strip().upper()

                    match sub_choice:
                        case 'P':
                            game.play_round()
                        case 'D':
                            game.deposit()
                        case 'S':
                            game.show_stats()
                        case 'Q':
                            print(f"\nThanks for playing! You leave with ${game.balance:.2f}")
                            break
                        case _:
                            print("Invalid option. Try again.")
            case 'W':
                import word_scramble
                word_scramble.NumberGuessingGame()
            case 'E':
                print("\nThank you for visiting. Goodbye!")
                break
            case _:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()

