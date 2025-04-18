---
layout: default
title: "classical.md"
permalink: /classical/
---

<!-- Classical Music Player -->
<h2>Classical Music Player</h2>

<audio id="bg-music" controls preload="auto">
  <source src="assets/music/PianoConcerto.ogg" type="audio/ogg">
  <!-- Add MP3 as fallback if you still have it -->
  <source src="assets/music/PianoConcerto.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

<button id="play-button" onclick="playMusic()">Play Music</button>

<div id="debug-info" style="margin-top: 20px; padding: 10px; border: 1px solid #ccc; display: none;">
  <h3>Debug Information</h3>
  <p id="status-message">Checking audio status...</p>
</div>

<script>
  // Wait for document to fully load
  document.addEventListener('DOMContentLoaded', function() {
    const audio = document.getElementById('bg-music');
    const debugInfo = document.getElementById('debug-info');
    const statusMessage = document.getElementById('status-message');
    
    // Show debug panel
    debugInfo.style.display = 'block';
    
    // Check if the audio file is accessible
    audio.addEventListener('loadeddata', function() {
      statusMessage.textContent = "Audio file loaded successfully. Duration: " + 
                                  Math.round(audio.duration) + " seconds";
      statusMessage.style.color = "green";
    });
    
    // Error handling
    audio.addEventListener('error', function(e) {
      let errorMessage = "Error loading audio file. ";
      
      if (audio.error) {
        switch(audio.error.code) {
          case 1:
            errorMessage += "The fetching process was aborted.";
            break;
          case 2:
            errorMessage += "Network error - the download was interrupted.";
            break;
          case 3:
            errorMessage += "Audio decoding failed - the file might be corrupted or unsupported.";
            break;
          case 4:
            errorMessage += "Audio source not found or access denied.";
            break;
          default:
            errorMessage += "Unknown error.";
        }
      }
      
      statusMessage.textContent = errorMessage;
      statusMessage.style.color = "red";
    });
  });

  function playMusic() {
    const audio = document.getElementById('bg-music');
    const statusMessage = document.getElementById('status-message');
    
    // Try to play and catch any errors
    audio.play().then(function() {
      statusMessage.textContent = "Audio is now playing.";
      statusMessage.style.color = "green";
    }).catch(function(error) {
      statusMessage.textContent = "Failed to play audio: " + error.message;
      statusMessage.style.color = "red";
      console.error("Audio playback error:", error);
    });
  }
</script>