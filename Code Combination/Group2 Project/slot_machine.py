"""
Auther: Shevanice Stephenson
ID: 2407727
Date: April 16, 2025
Reference: https://github.com/techwithtim/Python-Slot-Machine/blob/main/main.py#L1

Description: This Slot Machine game, developed in Python, allows users to input monetary
             values to deposit funds, place bets, and spin for a chance to win by matching
             symbols. The game simulates a real-world slot machine experience with visual
             elements, user interaction, and betting mechanics. It incorporates essential
             features such as dice rolls, random numbers, strings, lists, concatenation,
             Object-Oriented Programming (OOP) principles like objects and classes,
             exception handling, and descriptive analytics.
"""
import random
import statistics

class slotMachine():
    #variable declaration
    def __init__(self):
        self.symbols = ['🍒', '💎', '7', '🍋']
        self.symbol_counts = {'🍒': 4, '💎': 2, '7': 1, '🍋': 3}
        self.payouts = {'🍒': 2, '💎': 5, '7': 10, '🍋': 3}
        self.balance = 0.00
        self.max_lines = 3
        self.min_bet = 1.00
        self.max_bet = 1000.00
        self.rows = 3
        self.cols = 3
        self.total_betAmnt = 0.00
        self.history = []
     
    #deposit function 
    def deposit(self):
        while True:
            try:
                amount = float(input("\nWhat would you like to deposit? $"))
                if amount > 0:
                    self.balance += amount
                    print(f"Balance updated: ${self.balance}")
                    break
                else:
                    print("Deposit must be greater than $0.00.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    #slot machine spin function 
    def get_slotMachine_spin(self):
        all_symbols = []
        for symbol, symbol_count in self.symbol_counts.items():
            all_symbols.extend([symbol] * symbol_count)

        columns = []
        for _ in range(self.cols):
            column = []
            current_symbols = all_symbols[:]
            for _ in range(self.rows):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)
            columns.append(column)

        return columns
    
    #display slot machine function 
    def display_slotMachine(self, columns):
        print("\n Spinning...\n")
        for row in range(self.rows):
            print(" | ".join(columns[col][row] for col in range(self.cols)))
    
    #check user winnings function 
    def check_winnings(self, columns, lines, bet):
        winnings = 0
        winning_lines = []
        for line in range(lines):
            row_symbols = [columns[col][line] for col in range(self.cols)]
            if all(symbol == row_symbols[0] for symbol in row_symbols):
                symbol = row_symbols[0]
                win = self.payouts[symbol] * bet
                winnings += win
                winning_lines.append(line + 1)
        return winnings, winning_lines
     
    #number of betting lines function  
    def get_numberOFlines(self):
        while True:
            try:
                lines = int(input("\nEnter the number of lines to bet on (1 - " + str(self.max_lines) + ")? "))
                if 1 <= lines <= self.max_lines:
                    return lines
                else:
                    print("Enter a valid number of lines.")
            except ValueError:
                print("Invalid input. Please enter a number.")
     
    #betting amount function  
    def get_bet(self):
        while True:
            try:
                bet = float(input("\nWhat would you like to bet on each line? $"))
                if self.min_bet <= bet <= self.max_bet:
                    return bet
                else:
                    print(f"Amount must be between ${self.min_bet} - ${self.max_bet}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    #slot machine game play function 
    def play_round(self):
        if self.balance < self.min_bet:
            print("\nInsufficient balance to play.")
            return

        lines = self.get_numberOFlines()
        bet = self.get_bet()
        total_bet = bet * lines

        if total_bet > self.balance:
            print(f"\nInsufficient balance. You have ${self.balance}, but bet is ${total_bet}")
            return

        self.total_betAmnt += total_bet
        self.balance -= total_bet
        slots = self.get_slotMachine_spin()
        self.display_slotMachine(slots)

        winnings, winning_lines = self.check_winnings(slots, lines, bet)
        self.balance += winnings
        self.history.append(winnings)

        print(f"You won ${winnings}.")
        if winning_lines:
            print(f"You won on lines: {', '.join(map(str, winning_lines))}")
        else:
            print("No winning lines this time.")
        print(f"\nCurrent Balance: ${self.balance:.2f}")            

    #user statistical data function 
    def show_stats(self):
        if not self.history:
            print("\nNo games played yet.")
            return
        
        total_winnings = sum(self.history)
        total_loss = self.total_betAmnt - total_winnings

        print("\n------Game Stats------")
        print(f"Total games played: {len(self.history)}")
        print(f"Total winnings: ${total_winnings:.2f}")
        print(f"Total loss: ${total_loss:.2f}")
        print(f"Average per round: ${statistics.mean(self.history):.2f}")
        print(f"Max round winnings: ${max(self.history):.2f}")
        print(f"Min round winnings: ${min(self.history):.2f}")
