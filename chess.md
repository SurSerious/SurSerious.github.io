---
layout: chess
title: "Chess"
permalink: /chess/
---

{% raw %}
<!-- Container for the board -->
<div id="chessboard" style="width: 400px; height: 400px; margin: 20px auto; border: 1px solid #ccc;"></div>

<!-- Controls -->
<div style="text-align: center; margin: 20px;">
  <button id="prev-move">◀ Previous</button>
  <button id="next-move">Next ▶</button>
  <button id="flip-board">Flip Board</button>
</div>

<!-- Error display -->
<div id="chess-error" style="color: red; text-align: center;"></div>

<!-- Load REQUIRED CSS first -->
<link rel="stylesheet" href="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.css">

<script>
// Error handling
function showError(msg) {
  document.getElementById('chess-error').textContent = msg;
  console.error(msg);
}

// Check if ChessboardJS loaded
if (typeof Chessboard === 'undefined') {
  showError("ChessboardJS failed to load - loading now...");
  // Dynamically load if failed
  const css = document.createElement('link');
  css.rel = 'stylesheet';
  css.href = 'https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.css';
  document.head.appendChild(css);
  
  const script = document.createElement('script');
  script.src = 'https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.js';
  script.onload = initChess;
  document.head.appendChild(script);
} else {
  initChess();
}

function initChess() {
  try {
    // Initialize only if elements exist
    if (!document.getElementById('chessboard')) {
      showError("Chessboard element not found");
      return;
    }

    const board = Chessboard('chessboard', {
      position: 'start',
      showErrors: 'console'
    });
    
    document.getElementById('flip-board').addEventListener('click', () => board.flip());
    console.log("Chessboard initialized successfully");
    
  } catch (e) {
    showError("Error initializing chessboard: " + e.message);
  }
}
</script>
{% endraw %}