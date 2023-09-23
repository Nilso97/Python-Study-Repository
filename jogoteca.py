from flask import Flask, render_template, request, redirect

from Game import Game

app = Flask(__name__)

game_1 = Game(
    name='Tetris',
    category='Puzzle',
    console='Atari'
)
game_2 = Game(
    name='God of War',
    category='Rack n Slash',
    console='PS2'
)
game_3 = Game(
    name='Mortal Kombat',
    category='Luta',
    console='PS2'
)

games_list = [
    game_1, 
    game_2, 
    game_3
]

@app.route('/')
def list_games():
    return render_template('lista.html', title='Jogos', games=games_list)

@app.route('/novo-jogo')
def new_game():
    return render_template('novo-jogo.html', title='Novo Jogo')

@app.route('/criar', methods=['POST',])
def create():
    name = request.form['nome']
    category = request.form['categoria']
    console = request.form['console']
    games_list.append(Game(name=name, category=category, console=console))
    return redirect('/')

app.run(host='localhost', port=8080, debug=True)