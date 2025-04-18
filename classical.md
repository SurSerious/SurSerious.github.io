---
layout: default
title: "classical.md"
permalink: /classical/
---

<audio id="bg-music" loop>
  <source src="/assets/music/Piano_Concerto_No_21_in_C_Major.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

<button id="playMusic">Enable Music</button>

<script>
  const audio = document.getElementById('bg-music');

  document.getElementById('playMusic').addEventListener('click', () => {
    // Just to be sure, reset currentTime and muted state
    audio.currentTime = 0;
    audio.muted = false;

    audio.play()
      .then(() => {
        console.log('Audio playback started.');
      })
      .catch(err => {
        console.error('Playback failed:', err);
      });
  });
</script>
