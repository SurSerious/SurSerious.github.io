---
layout: chess
title: "Chess"
permalink: /chess/
---

<style>
  /* General styling for the page */
  .chess-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  
  /* Style for the chess board container */
  .chess-board-container {
    width: 100%;
    max-width: 600px;
    margin: 30px auto;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  }
  
  h1 {
    text-align: center;
    margin-bottom: 30px;
  }
</style>

<div class="chess-container">
  <h1>One of my recent games of chess</h1>
  
  <p>Here's one of my recent games:</p>
  
  <div class="chess-board-container">
    <div id="chess-board"></div>
  </div>
  
  <p>Additional content about the game can go here...</p>
</div>

<script src="https://www.chess.com/pgnviewer.js"></script>
<script>
  document.addEventListener('DOMContentLoaded', function() {
    var game = new PgnViewer({
      boardId: 'chess-board',
      gameId: '123442777160',
      showCoords: true,
      width: '100%'
    });
  });
</script>