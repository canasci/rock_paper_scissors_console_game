import random
import time
import sys
from abc import ABC, abstractmethod


class GameItems:

    context_dict = {'rock': {'beats': "scissors", 'ties': "rock", 'loses_against': "paper"},
                    'paper': {'beats': "rock", 'ties': "paper", 'loses_against': "scissors"},
                    'scissors': {'beats': "paper", 'ties': "scissors", 'loses_against': "rock"}
                    }

    def __init__(self, key):
        self.name = key
        self.beats = self.context_dict[key]['beats']
        self.ties = self.context_dict[key]['ties']
        self.loses_against = self.context_dict[key]['loses_against']

    def __str__(self):
        return self.name.upper()


class Rock(GameItems):

    def __init__(self, key):
        super().__init__(key)


class Paper(GameItems):

    def __init__(self, key):
        super().__init__(key)


class Scissors(GameItems):

    def __init__(self, choice):
        super().__init__(choice)


class Player(ABC):

    def __init__(self, name='', choice=''):
        self.name = name
        self.choice = choice

    @abstractmethod
    def action(self):
        pass


class User(Player):

    def __init__(self):
        super().__init__(name='', choice='')

    def action(self):
        if self.choice == 'rock':
            return Rock(self.choice)
        elif self.choice == 'paper':
            return Paper(self.choice)
        elif self.choice == 'scissors':
            return Scissors(self.choice)


class Computer(Player):

    def __init__(self):
        super().__init__(name='', choice='')

    def action(self):
        self.choice = random.randint(1, 3)
        if self.choice == 1:
            self.choice = 'rock'
            return Rock(self.choice)
        elif self.choice == 2:
            self.choice = 'paper'
            return Paper(self.choice)
        else:
            self.choice = 'scissors'
            return Scissors(self.choice)


class RpsGame:

    def __init__(self):
        self.player1 = User()
        self.player2 = Computer()
        self.game_count = 1
        self.player1_wins = 0
        self.player2_wins = 0

    def start_game(self):
        if self.game_count == 1:
            print("ROCK, PAPER, SCISSORS\n\nGame {} Starting...\n ".format(self.game_count))
            self.player1.name = input("Please enter your name: ")
        else:
            print("\nGame {} Starting...\n".format(self.game_count))

        self.player1.choice = str.lower(input("Please choose your move,"
                                              " {} (Rock, Paper, Scissors): ".format(self.player1.name)))
        while self.player1.choice not in ['rock', 'paper', 'scissors']:
            self.player1.choice = input("Please enter a valid move, "
                                        "(Rock, Paper, or Scissors): ".format(self.player1.name)).lower()

    def play(self):
        return {'User': self.player1.action(), 'Computer': self.player2.action()}

    def game_result(self):
        moves = self.play()
        print("\nUser played {0}, \nComputer played {1}".format(moves['User'], moves['Computer']))

        if moves["User"].name in moves["Computer"].loses_against:
            self.player1_wins += 1
            return "\nUser wins! {0} beats {1}".format(self.player1.choice.upper(), self.player2.choice.upper())

        elif moves["User"].name in moves["Computer"].beats:
            self.player2_wins += 1
            return "\nComputer wins! {1} beats {0} \nEZ PZ!".format(self.player1.choice.upper(), self.player2.choice.upper())

        elif moves["User"].name in moves["Computer"].name:
            return "\nGame tied! NICE TRY!"

    def play_again(self):
        user_decision = input("\nWould you like to play again? [y/n]:\n").lower()

        while user_decision not in ['yes', 'no', 'y', 'n']:
            user_decision = input("Please enter 'y' for 'Yes', 'n' for 'No'!\n")

        if user_decision == 'n':
            print("\nUser won {0} of the {1} game/s played!".format(self.player1_wins, self.game_count))
            print("Thank you for playin', NOOB!\n")
            exit_key = "exit"
            while exit_key != "":
                exit_key = input("Please press 'Enter' to exit the game!")
            print("\nProcess terminating...")
            time.sleep(3)   # program sleeps 3 seconds before program exits!
            sys.exit(0)

        elif user_decision == 'y':
            self.game_count += 1
            self.start_game()
            self.play()
            print(self.game_result())
            self.play_again()


if __name__ == '__main__':
    game = RpsGame()
    game.start_game()
    game.play()
    print(game.game_result())
    game.play_again()
