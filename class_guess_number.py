import random

class GuessNumberGame:
    number_to_guess: int

    def __init__(self):
        self.number_to_guess: int  = 0
        self.user_input: int = 0
        self.player_guessed: bool = False
        self.attempt: int = 1

    def generate_number(self):
        self.number_to_guess = random.randint(1,10)
    
    def get_user_input(self, help_string: str):
        while True:
            try:
                self.user_input = int(input(help_string))

                break
            except ValueError as e:
                    print(f"Error: Wrong input {e}")

    def check_user_input(self):
        self.player_guessed = self.user_input == self.number_to_guess

    def get_next_input_hint(self) -> str:
        if self.user_input > self.number_to_guess:
            return "Try smaller number: "
        else:
            return "Try higher number: "

    def print_attempt_number_hint(self) -> str:
         print(f"It`s your {self.attempt} attempt.")
    
    def increase_attempt_number(self) -> int:
        self.attempt += 1 
    
    def play(self):
        self.generate_number()
        print(self.number_to_guess)
        self.get_user_input("Guess the number from 1 to 10: ")
        while not self.player_guessed:
            self.increase_attempt_number()
            self.print_attempt_number_hint()
            hint: str = self.get_next_input_hint()
            self.get_user_input(hint)
            self.check_user_input()

        print("You won this game")


game = GuessNumberGame()
game.play()
