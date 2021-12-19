import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo
print(logo)

display = []
for _ in range(word_length):
    display += "_"
print(f"\n{display}")
print(f"\nGuess the word containing {len(display)} words.")

while not end_of_game:
    guess = input("\nGuess a letter here: ").lower()

    if guess in display:
        print(f"\nYou've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
  
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nYou lose.😥")
            print(f"\nThe word was '{chosen_word}'")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("\nBravo! You win.😍")

    from hangman_art import stages
    print(stages[lives])