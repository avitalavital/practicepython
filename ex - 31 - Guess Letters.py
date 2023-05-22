"""
the word is "EVAPORATE"
give the use a clue word - the length of the word. example:  _ _ _ _ _
ask the user for a letter
check if the letter is in the word
if the letter is in the word place the letter in the correct location in the clue word
print the new clue word
if the letter isn't in the word print a massage. bonus: add 1 to the error counter
bonus: if the player guesses the same letter again display a message about it
do it until all the letters have been guessed. bonus:the error counter gets to 6
"""
word = "evaporate"
clue_word = ["_"] * len(word)
error_counter = 0
previous_guesses = []
print("Welcome to Hangman!")
print(''.join(clue_word))

while "_" in clue_word and error_counter < 6:
    guess_letter = input("Guess your letter ")
    if guess_letter in previous_guesses:
        print(f"you have guessed this letter before \nthese are your previous guesses {previous_guesses}")
    elif guess_letter in word:
        print("good!")
        # clue_word = [my_letter if x == my_letter else '_' for x in word]
        for i in range(len(word)):
            if word[i] == guess_letter:
                clue_word[i] = guess_letter
        print(''.join(clue_word))
    else:
        print("Incorrect!")
        print(''.join(clue_word))
        error_counter += 1
        print(f"you have {error_counter} errors")
        previous_guesses.append(guess_letter)
print("your out of attempts")
