from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Store game state in a simple dictionary
games = {}

@app.route('/')
def home():
    return render_template('game.html')

@socketio.on('join_game')
def on_join(data):
    room = data['room']
    join_room(room)
    emit('player_joined', {'msg': 'A new player has joined'}, room=room)

@socketio.on('roll_dice')
def roll_dice(data):
    room = data['room']
    die_roll = random.randint(1, 6)
    emit('dice_rolled', {'result': die_roll}, room=room)

# Define other game logic events like token movement, turn rotation, etc.

if __name__ == '__main__':
    socketio.run(app, debug=True)
