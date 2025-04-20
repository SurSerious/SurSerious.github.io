---
layout: chess
title: "Chess"
permalink: /chess/
---

{% raw %}
<!-- Chessboard container -->
<div id="chessboard" style="width: 400px; height: 400px; margin: 20px auto;"></div>

<!-- Controls -->
<div style="text-align: center; margin: 20px;">
  <button id="prev-move">◀ Previous</button>
  <button id="next-move">Next ▶</button>
  <button id="flip-board">Flip Board</button>
</div>

<!-- Load dependencies -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.12.0/chess.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.js"></script>

<script>
$(document).ready(function() {
  // Initialize board with proper piece images
  const board = Chessboard('chessboard', {
    position: 'start',
    draggable: true,
    pieceTheme: 'https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/img/chesspieces/wikipedia/{piece}.png',
    showErrors: 'console'
  });

  // Initialize game
  const game = new Chess();
  let currentMove = -1;
  const moves = [];

  // Load your game
  const pgn = [
    '[Event "SolitaryLife1 vs. wweaamm"]',
    '1. e4 e5 2. Nf3 Nc6 3. c3 Nf6 4. Qa4 d5 5. exd5 Nxd5 6. d4 Bd6 7. dxe5 Bxe5',
    '8. Nxe5 Qe7 9. Qe4 Nxe5 10. Qxd5 Nf3+ 11. Kd1 Qe1+ 12. Kc2 Bf5+ 13. Qxf5 Qxf2+',
    '14. Nd2 Rd8 15. Qxf3 Rxd2+ 16. Bxd2 Qxf3 17. gxf3 1-0'
  ].join('\n');

  if (game.load_pgn(pgn)) {
    moves.push(...game.history({verbose: true}));
    updateBoard();
  } else {
    console.error("PGN loading failed");
  }

  // Navigation functions
  function updateBoard() {
    const tempGame = new Chess();
    for (let i = 0; i <= currentMove; i++) {
      tempGame.move(moves[i]);
    }
    board.position(tempGame.fen());
  }

  $('#prev-move').click(() => {
    if (currentMove > -1) currentMove--;
    updateBoard();
  });

  $('#next-move').click(() => {
    if (currentMove < moves.length - 1) currentMove++;
    updateBoard();
  });

  $('#flip-board').click(() => board.flip());
});
</script>

<style>
/* Board styling */
#chessboard {
  box-shadow: 0 5px 15px rgba(0,0,0,0.3);
  background-color: #f0d9b5;
}

/* Button styling */
button {
  padding: 8px 15px;
  margin: 0 5px;
  background: #4a6ea9;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background: #3a5a8a;
}
</style>
{% endraw %}