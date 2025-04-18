---
layout: default
title: "classical.md"
permalink: /classical/
---

<audio id="bg-music" loop>
  <source src="/assets/music/Piano Concerto No. 21 in C Major.mp3" type="audio/mpeg">
</audio>

<script>
  window.addEventListener('load', function () {
    const audio = document.getElementById('bg-music');
    audio.play().catch(error => {
      console.log('Autoplay was prevented:', error);
    });
  });
</script>
