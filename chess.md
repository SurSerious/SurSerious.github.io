---
layout: chess
title: "Chess"
permalink: /chess/
---

{% raw %}
<!-- Chessboard container - must have explicit dimensions -->
<div id="chessboard" style="width: 400px; height: 400px; margin: 20px auto;"></div>

<!-- Load dependencies in correct order -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.2/chess.js"></script>

<script>
// Initialize after all dependencies are loaded
$(document).ready(function() {
  try {
    const board = Chessboard('chessboard', {
      position: 'start',
      draggable: true
    });
    
    console.log("Chessboard initialized successfully!");
    
    // Load your game
    const game = new Chess();
    const pgn = `
[Event "SolitaryLife1 vs. wweaamm"]
1. e4 e5 2. Nf3 Nc6 3. c3 Nf6 4. Qa4 d5 5. exd5 Nxd5 6. d4 Bd6 7. dxe5 Bxe5 8.
Nxe5 Qe7 9. Qe4 Nxe5 10. Qxd5 Nf3+ 11. Kd1 Qe1+ 12. Kc2 Bf5+ 13. Qxf5 Qxf2+ 14.
Nd2 Rd8 15. Qxf3 Rxd2+ 16. Bxd2 Qxf3 17. gxf3 1-0
`;
    game.loadPgn(pgn);
    board.position(game.fen());
    
  } catch (e) {
    console.error("Initialization error:", e);
    alert("Chessboard failed to load. Check console for details.");
  }
});
</script>
{% endraw %}