from flask import Flask, render_template, request
import random
from data import fall

app = Flask(__name__)

def get_random_word():
    random_word = random.choice(list(fall.keys()))
    return random_word

random_word = get_random_word()
win = False
guessed_word = "*" * len(random_word)
letters_guessed_already = set()

@app.route('/')
def index():
    return render_template('index.html', player_guesses=guessed_word)

@app.route('/play', methods=['POST'])
def play():
    global random_word, win, guessed_word, letters_guessed_already
    user_guess = request.form.get('user_guess').lower()
    message_to_user = ""
    
    number_of_guesses = len(random_word) - 2
    
    print(number_of_guesses)
    print(random_word)
    print(guessed_word)
    
    while number_of_guesses > 0:
        if user_guess.lower() == random_word.lower():
            message_to_user = f'You Won, You guessed the word {random_word}'
            win = True
            break
        elif user_guess.lower() in random_word.lower():
            letters_guessed_already.add(user_guess)
            guessed_word_temp = ""
            for i in range(len(random_word)):
                if random_word[i].lower() == user_guess.lower():
                    guessed_word_temp += random_word[i]
                else:
                    guessed_word_temp += guessed_word[i]
                    
            guessed_word = guessed_word_temp
            message_to_user = f"You correctly guessed {guessed_word}"
        else:
            letters_guessed_already.add(user_guess)
            message_to_user = f"Sorry you guessed wrong. Try Again! {guessed_word}"
        number_of_guesses -= 1
        
    if win:
        random_word = get_random_word()
        win = False
        guessed_word = "*" * len(random_word)
        letters_guessed_already = set()

    return render_template('index.html', message_to_user=message_to_user, letters_guessed=letters_guessed_already)

if __name__ == '__main__':
    app.run(debug=True)