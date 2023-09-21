from data import fall
import random 

random_word = random.choice(list(fall.keys()))
guessed_word = "*" * len(random_word)
number_of_guesses = len(random_word)

while number_of_guesses > 0:
    print(random_word)
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
    
    if number_of_guesses == 0 and guessed_word == random_word:
        print(f'You Won, You guessed the word {random_word}')
    elif number_of_guesses == 0:
        print("You Lost")
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# def choose_a_category():
#     print()
    
# def prompt_player():
#         user_guess = input("Enter in a letter or enter in a word to guess => ")
#         return user_guess

# def get_random_word():
#     random_word = random.choice(list(fall.keys()))
#     return random_word

# message_to_user = ""
# random_word = get_random_word()

# def player_guesses():
#     print(random_word)
#     guessed_word = "*" * len(random_word)
#     return guessed_word
    
# def play_game(user_guess):
#     number_of_guesses = len(random_word)
#     guessed_word = "*" * len(random_word)
    
#     print(number_of_guesses)
#     print(random_word)
#     print(guessed_word)
#     while number_of_guesses > 0:
#         if user_guess.lower() == random_word.lower():
#             message_to_user = f'You Won, You guessed the word {random_word}'
#             break
#         elif user_guess.lower() in random_word.lower():
#             guessed_word_temp = ""
#             for i in range(len(random_word)):
#                 if random_word[i].lower() == user_guess.lower():
#                     guessed_word_temp += random_word[i]
#                 else:
#                     guessed_word_temp += guessed_word[i]
                    
#             guessed_word = guessed_word_temp
#             message_to_user = f"You correctly guessed {guessed_word}"
#         else:
#             message_to_user = f"Sorry you guessed wrong. Try Again! {guessed_word}"
#         number_of_guesses -= 1
#     return message_to_user
    