---
layout: default
title: "classical.md"
permalink: /classical/
---

<!-- Classical Music Player -->
<h2>Classical Music Player</h2>

<audio id="bg-music" controls>
  <source src="./assets/music/Piano_Concerto_No_21_in_C_Major.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

<button id="play-button" onclick="playMusic()">Play Music</button>

<p id="error-message" style="color: red; display: none;">Error loading audio file. Please check that the file exists at the correct path.</p>

<script>
  function playMusic() {
    const audio = document.getElementById('bg-music');
    const errorMsg = document.getElementById('error-message');
    
    // Try to play and catch any errors
    audio.play().catch(error => {
      console.error("Audio playback error:", error);
      errorMsg.style.display = "block";
    });
  }
  
  // Check if audio file is available
  document.getElementById('bg-music').addEventListener('error', function() {
    document.getElementById('error-message').style.display = "block";
  });
</script>