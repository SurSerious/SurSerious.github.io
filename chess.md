---
layout: chess
title: "Chess"
permalink: /chess/
---

<script>
  $(document).ready(function () {
    const board = Chessboard('chessboard', {
      position: 'start',
      draggable: true,
      pieceTheme: 'https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/img/chesspieces/wikipedia/{piece}.png',
    });

    const game = new Chess();
    let currentMove = -1;
    const moves = [];

    const pgn = `
      [Event "SolitaryLife1 vs. wweaamm"]
      1. e4 e5 2. Nf3 Nc6 3. c3 Nf6 4. Qa4 d5 5. exd5 Nxd5 6. d4 Bd6 7. dxe5 Bxe5
      8. Nxe5 Qe7 9. Qe4 Nxe5 10. Qxd5 Nf3+ 11. Kd1 Qe1+ 12. Kc2 Bf5+ 13. Qxf5 Qxf2+
      14. Nd2 Rd8 15. Qxf3 Rxd2+ 16. Bxd2 Qxf3 17. gxf3 1-0
    `;

    if (game.load_pgn(pgn)) {
      moves.push(...game.history({ verbose: true }));
      updateBoard();
    }

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