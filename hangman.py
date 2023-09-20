from data import fall
import random 

random_word = random.choice(list(fall.keys()))
guessed_word = "*" * len(random_word)
number_of_guesses = len(random_word)

while number_of_guesses > 0:
    user_guess = input("Enter in a letter or enter in a word to guess => ")
    
    if user_guess.lower() == random_word.lower():
        print(f'You Won, You guessed the word {random_word}')
        break
    elif user_guess.lower() in random_word.lower():
        guessed_word_temp = ""
        for i in range(len(random_word)):
            if random_word[i].lower() == user_guess.lower():
                guessed_word_temp += random_word[i]
            else:
                guessed_word_temp += guessed_word[i]
                
        guessed_word = guessed_word_temp
        
        print(f"You correctly guessed {guessed_word}")
    else:
        print("Sorry you guessed wrong. Try Again!")
        print(guessed_word)
    number_of_guesses -= 1