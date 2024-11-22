from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import random
from words import word_list

app = Flask(__name__)
app.secret_key = 'hangman_secret_key'

MAX_TRIES = 7

def start_new_game():
    word = random.choice(word_list).upper()
    return {
        'word': word,
        'guesses': [],
        'tries_left': MAX_TRIES,
        'current_word': ['_' for _ in word],
    }

@app.route('/')
def index():
    session['game'] = start_new_game()
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    game = session.get('game', None)
    if not game:
        return jsonify({'error': 'Game not found!'}), 400

    letter = request.form.get('letter', '').upper()
    if letter in game['guesses']:
        return jsonify({'error': 'Letter already guessed!'}), 400
    
    game['guesses'].append(letter)

    if letter in game['word']:
        for idx, char in enumerate(game['word']):
            if char == letter:
                game['current_word'][idx] = letter
    else:
        game['tries_left'] -= 1

    session['game'] = game

    if game['tries_left'] == 0:
        return jsonify({'game_over': True, 'status': 'lost', 'word': game['word']})
    elif ''.join(game['current_word']) == game['word']:
        return jsonify({'game_over': True, 'status': 'won', 'word': game['word']})
    else:
        return jsonify({
            'current_word': ''.join(game['current_word']),
            'tries_left': game['tries_left'],
            'guesses': game['guesses'],
        })

@app.route('/game_over')
def game_over():
    status = request.args.get('status', 'lost')
    word = request.args.get('word', '')
    return render_template('game_over.html', status=status, word=word)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
