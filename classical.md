---
layout: default
title: "classical.md"
permalink: /classical/
---

## Welcome to My Classical Music Page

Click below to play the music.

<audio id="bg-music" loop>
  <source src="/assets/music/Piano_Concerto_No_21_in_C_Major.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

<button id="playMusic">Play Music</button>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById('playMusic');
    const audio = document.getElementById('bg-music');

    button.addEventListener('click', function () {
      audio.currentTime = 0;  // Start from the beginning
      audio.muted = false;    // Make sure it's not muted
      audio.play()            // Attempt to play the audio
        .then(() => {
          console.log('Music is playing!');
        })
        .catch(err => {
          console.error('Play failed:', err);
          alert('Browser is blocking audio playback. Try tapping anywhere on the page.');
        });
    });
  });
</script>
