---
layout: default
title: "classical.md"
permalink: /classical/
---

## Welcome to My Page

Click the button below to play music.

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
      audio.currentTime = 0;
      audio.muted = false;

      audio.play().then(() => {
        console.log('Music is playing!');
      }).catch(err => {
        console.error('Play failed:', err);
        alert('Your browser is blocking audio playback. Tap the page or allow autoplay.');
      });
    });
  });
</script>
