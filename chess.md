---
layout: chess
title: "Chess"
permalink: /chess/
---

# My Game vs. wweaamm

{% raw %}
<div id="chessboard" style="width: 70vw; max-width: 600px; margin: 20px auto;"></div>
<div id="move-controls" style="max-width: 600px; margin: 0 auto; text-align: center;">
  <button id="prev-move" style="margin: 5px;">◀ Previous</button>
  <button id="next-move" style="margin: 5px;">Next ▶</button>
  <button id="flip-board" style="margin: 5px;">Flip Board</button>
</div>
<div id="move-list" style="max-width: 600px; margin: 20px auto; columns: 2; column-gap: 20px;"></div>

<!-- Load chess libraries -->
<link rel="stylesheet" href="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.2/chess.js"></script>
<script src="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.js"></script>

<script>
// Initialize game
const game = new Chess();
const board = Chessboard('chessboard', {
  position: 'start',
  draggable: false,
  moveSpeed: 'fast'
});

// Your exact game in PGN format
const pgn = `
[Event "SolitaryLife1 vs. wweaamm"]
[Site "Chess.com"]
[Date "2025-03-02"]
[White "SolitaryLife1"]
[Black "wweaamm"]
[Result "1-0"]
[WhiteElo "1213"]
[BlackElo "1052"]
[TimeControl "600"]
[Termination "SolitaryLife1 won by resignation"]
1. e4 e5 2. Nf3 Nc6 3. c3 Nf6 4. Qa4 d5 5. exd5 Nxd5 6. d4 Bd6 7. dxe5 Bxe5 8.
Nxe5 Qe7 9. Qe4 Nxe5 10. Qxd5 Nf3+ 11. Kd1 Qe1+ 12. Kc2 Bf5+ 13. Qxf5 Qxf2+ 14.
Nd2 Rd8 15. Qxf3 Rxd2+ 16. Bxd2 Qxf3 17. gxf3 1-0
`;

// Load the game
game.loadPgn(pgn);
const moves = game.history({ verbose: true });
let currentMove = -1;

// Display all moves
const movesElement = document.getElementById('move-list');
moves.forEach((move, i) => {
  const moveNumber = Math.floor(i/2) + 1;
  if (i % 2 === 0) {
    movesElement.innerHTML += `<div><strong>${moveNumber}.</strong> <span class="move" data-move="${i}">${move.san}</span>`;
  } else {
    movesElement.innerHTML += ` <span class="move" data-move="${i}">${move.san}</span></div>`;
  }
});

// Update board position
function updateBoard() {
  const tempGame = new Chess();
  for (let i = 0; i <= currentMove; i++) {
    tempGame.move(moves[i]);
  }
  board.position(tempGame.fen());
  
  // Highlight current move
  document.querySelectorAll('.move').forEach(el => el.style.fontWeight = 'normal');
  if (currentMove >= 0) {
    document.querySelector(`.move[data-move="${currentMove}"]`).style.fontWeight = 'bold';
  }
}

// Navigation controls
document.getElementById('prev-move').addEventListener('click', () => {
  if (currentMove > -1) currentMove--;
  updateBoard();
});

document.getElementById('next-move').addEventListener('click', () => {
  if (currentMove < moves.length - 1) currentMove++;
  updateBoard();
});

document.getElementById('flip-board').addEventListener('click', () => {
  board.flip();
});

// Click move in notation
document.querySelectorAll('.move').forEach(el => {
  el.addEventListener('click', (e) => {
    currentMove = parseInt(e.target.getAttribute('data-move'));
    updateBoard();
  });
});

// Initialize
updateBoard();
</script>

<style>
#chessboard { 
  box-shadow: 0 5px 15px rgba(0,0,0,0.5);
  margin-bottom: 20px;
}
.move {
  cursor: pointer;
  padding: 2px 5px;
  border-radius: 3px;
  display: inline-block;
}
.move:hover {
  background: rgba(0,0,0,0.1);
}
button {
  padding: 5px 10px;
  background: #f0f0f0;
  border: 1px solid #ccc;
  border-radius: 3px;
  cursor: pointer;
}
button:hover {
  background: #e0e0e0;
}
</style>
{% endraw %}