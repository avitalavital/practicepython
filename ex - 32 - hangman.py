import random

words = open("words").read().split()
# print(random.choice(words))
while True:
    word = random.choice(words)
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
    print(f"your out of attempts \n {word}")
