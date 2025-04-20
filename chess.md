---
layout: chess
title: "Chess"
permalink: /chess/
---

# One of my recent games of chess

<div id="chessboard" style="width: 70vw; max-width: 600px; margin: 20px auto;"></div>
<div id="game-moves" style="max-width: 600px; margin: 0 auto;"></div>
<div id="move-notes" style="max-width: 600px; margin: 20px auto; background: rgba(255,255,255,0.8); padding: 15px; border-radius: 5px;"></div>

<!-- Load chess libraries -->
<link rel="stylesheet" href="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.2/chess.js"></script>
<script src="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.js"></script>

<script>
// Initialize game
const game = new Chess();
const board = Chessboard('chessboard', {
  position: 'start',
  draggable: true
});

// Your game in PGN format (replace with your moves)
const pgn = `
[Event "My Chess Game"]
[Site "Your Website"]
1. e4 {Best opening move!} e5 2. Nf3 {Developing knight} Nc6 
3. Bb5 {Ruy Lopez} a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 O-O *
`;

// Load the game
game.loadPgn(pgn);
board.position(game.fen());

// Display moves and notes
const movesElement = document.getElementById('game-moves');
const notesElement = document.getElementById('move-notes');
let moveCount = 0;

game.history({ verbose: true }).forEach((move, i) => {
  // Show move notation
  if (i % 2 === 0) {
    moveCount++;
    movesElement.innerHTML += `<span class="move-number">${moveCount}.</span>`;
  }
  movesElement.innerHTML += `<span class="move" data-move="${i}">${move.san}</span> `;
  
  // Show notes if available
  if (move.comment) {
    notesElement.innerHTML += `<p><strong>Move ${moveCount}${i % 2 === 0 ? '' : '...'}:</strong> ${move.san}<br>${move.comment}</p>`;
  }
});

// Add click handlers for moves
document.querySelectorAll('.move').forEach(element => {
  element.addEventListener('click', (e) => {
    const moveIndex = parseInt(e.target.getAttribute('data-move'));
    const tempGame = new Chess();
    game.history({ verbose: true }).slice(0, moveIndex + 1).forEach(m => {
      tempGame.move(m);
    });
    board.position(tempGame.fen());
  });
});
</script>

<style>
#chessboard { 
  box-shadow: 0 5px 15px rgba(0,0,0,0.5);
  margin-bottom: 20px;
}
.move-number {
  font-weight: bold;
  margin-right: 5px;
}
.move {
  cursor: pointer;
  padding: 2px 5px;
  border-radius: 3px;
}
.move:hover {
  background: #ddd;
}
</style>