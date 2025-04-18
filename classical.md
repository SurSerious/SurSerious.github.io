---
layout: default
title: "classical.md"
permalink: /classical/
---

<audio id="bg-music" loop muted>
  <source src="/assets/music/Piano_Concerto_No_21_in_C_Major.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

<button id="playMusic">Play Music</button>

<script>
  const audio = document.getElementById('bg-music');

  // Attempt to autoplay silently
  window.addEventListener('load', function () {
    audio.play().then(() => {
      console.log('Autoplay started (muted)');
    }).catch(error => {
      console.log('Autoplay was prevented:', error);
    });
  });

  // Button to unmute and play
  document.getElementById('playMusic').addEventListener('click', function () {
    audio.muted = false;
    audio.play().then(() => {
      console.log('Playback started after unmuting');
    }).catch(err => {
      console.log('Playback failed:', err);
    });
  });
</script>
