---
layout: default
title: "classical.md"
permalink: /classical/
---

## Classical Music Player

Click below to enable and play the music.

<audio id="bg-music" loop muted>
  <source src="/assets/music/Piano_Concerto_No_21_in_C_Major.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

<button id="playMusic">Play Music</button>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById('playMusic');
    const audio = document.getElementById('bg-music');

    button.addEventListener('click', function () {
      // Start audio from the beginning and unmute
      audio.currentTime = 0;
      audio.muted = false;

      // Attempt to play the audio after user clicks
      audio.play()
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
