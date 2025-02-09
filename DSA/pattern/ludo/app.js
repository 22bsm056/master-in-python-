const socket = io();

function rollDice() {
    socket.emit('roll_dice', { room: 'game1' });
}

socket.on('dice_rolled', (data) => {
    document.getElementById('dice-result').innerText = 'Dice result: ' + data.result;
    // Update the game state here
});

socket.on('player_joined', (data) => {
    alert(data.msg);
});
