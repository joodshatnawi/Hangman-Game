import random
chosen_word = ""
hidden_word = ""
letter=""
guessed_letters = [] 
attempts = 6
hint_used = False 
score=0

def load_words():
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    return words

secret_word = load_words()
def choose_word():
    global hidden_word
    global chosen_word

    chosen_word = random.choice(secret_word)
    hidden_word = "*" * len(chosen_word)

def replace_star(letter):
    global hidden_word
    new_hidden = ""
    flag = False
    for idex in range(len(chosen_word)):
        if chosen_word[idex] == letter:
            new_hidden += letter
            flag = True
        else:
            new_hidden += hidden_word[idex]  
    hidden_word = new_hidden
    return flag

def draw_hangman(attempts_left):
    stages = [
        """
         -----
         |   |
             |
             |
             |
      =========
        """,
        """
         -----
         |   |
         O   |
             |
             |
      =========
        """,
        """
         -----
         |   |
         O   |
        /|   |
             |
      =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
             |
      =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        /    |
      =========
        """,
        """
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
      =========
        """
    ]

    mistakes = 6 - attempts_left
    if mistakes > 5:
        mistakes = 5

    print(stages[mistakes])

    
def display_status():
    print("\nCurrent word:", " ".join(hidden_word))
    print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")
    print(f"Attempts left: {attempts}")



def get_guess():
    
    global guessed_letters
    while True:
        letter = input("Enter a letter: ").lower()
        if len(letter) != 1 or not letter.isalpha():
            print(" Invalid input! Please enter one letter only.")
            continue
        if letter in guessed_letters:
            print(f" You already guessed '{letter}'. Try another one.")
            continue
        guessed_letters.append(letter)
        return letter

def attempt():
    global score
    global attempts 
    global hint_used

    if not hint_used:
        want_hint = input("Do you want a hint? (y/n): ").lower()
        if want_hint == 'y':
            use_hint()

    while "*" in hidden_word and attempts > 0:
        letter = get_guess()
        found = replace_star(letter)
        display_status()

        if not found:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left, choose another letter:")
            draw_hangman(attempts)
    if "*" not in hidden_word:
        end_game_message(True)
    else:
        end_game_message(False)

        
    
def use_hint():
    global attempts
    global hint_used
    if not hint_used:
        print(f"Hint: The first letter of the word is '{chosen_word[0]}'")
        hint_used = True
        attempts -= 1
        print(f"You used a hint! You have {attempts} attempts left.")

def end_game_message(won):
    global score
    if won:
        print(f" Congratulations! You guessed the word: {chosen_word}")
        score += 10
    else:
        print(f" Game over! The word was '{chosen_word}'")
        score -= 5
        if score < 0:
            score = 0
    print(f"Your current score: {score}")



   
def reset_game():
    global guessed_letters
    global chosen_word
    global hidden_word
    global hint_used
    global attempts
    guessed_letters = []
    chosen_word = ""
    hidden_word = ""
    hint_used = False
    attempts = 6


def play_game():
    while True:
        reset_game()
        choose_word()
        attempt()

        again = input("Do you want to play again? (y/n): ").lower()
        if again == 'n':
            print(f"Final score : {score}")
            print("Thanks for playing! Goodbye ")
            break
        elif again != 'y':
            print("Please enter y or n only.")
        
play_game()