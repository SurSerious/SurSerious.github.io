---
layout: default
title: "classical.md"
permalink: /classical/
---

<audio id="bg-music" loop>
  <source src="/assets/music/Piano_Concerto_No_21_in_C_Major.mp3" type="audio/mpeg">
</audio>

<button id="playMusic">Play Music</button>

<script>
  document.getElementById('playMusic').addEventListener('click', function () {
    const audio = document.getElementById('bg-music');
    audio.play().then(() => {
      console.log('Playback started');
    }).catch((err) => {
      console.log('Playback failed:', err);
    });
  });

  // Try autoplay on page load (may be blocked, but still worth attempting)
  window.addEventListener('load', function () {
    const audio = document.getElementById('bg-music');
    audio.play().catch(error => {
      console.log('Autoplay was prevented:', error);
    });
  });
</script>

