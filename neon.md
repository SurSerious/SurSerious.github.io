---
layout: neon
title: "neon.md"
permalink: /neon/
---

<style>
  h1.rainbow-title {
    font-size: 3.5rem;
    font-weight: bold;
    text-align: center;
    padding: 20px;
    margin: 30px 0 15px 0;
    animation: rainbow-glow 8s linear infinite;
    text-shadow: 0 0 10px currentColor, 0 0 20px currentColor, 0 0 30px currentColor;
    font-family: 'Arial', sans-serif;
  }

  @keyframes rainbow-glow {
    0% { color: #ff0000; text-shadow: 0 0 10px #ff0000, 0 0 20px #ff0000, 0 0 30px #ff0000; }
    16.6% { color: #ff8800; text-shadow: 0 0 10px #ff8800, 0 0 20px #ff8800, 0 0 30px #ff8800; }
    33.3% { color: #ffff00; text-shadow: 0 0 10px #ffff00, 0 0 20px #ffff00, 0 0 30px #ffff00; }
    50% { color: #00ff00; text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 30px #00ff00; }
    66.6% { color: #00ffff; text-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 30px #00ffff; }
    83.3% { color: #0088ff; text-shadow: 0 0 10px #0088ff, 0 0 20px #0088ff, 0 0 30px #0088ff; }
    100% { color: #ff00ff; text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 30px #ff00ff; }
  }

  .rainbow-footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 50px; /* Adjust based on your GIF's height */
    overflow: hidden;
    z-index: 100;
  }

  .rainbow-footer-gif {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: bottom;
  }

  /* Make sure content doesn't hide behind the footer */
  .page-content {
    margin-bottom: 60px; /* Should be slightly more than the footer height */
  }
</style>

<div class="page-content">
  <h1 class="rainbow-title">Neon Dreams Only A Moment Away</h1>

  <p>This is your neon-themed page content. The rainbow GIF will now appear at the bottom edge of the page.</p>
</div>

<div class="rainbow-footer">
  <img src="https://gifdb.com/images/high/rainbow-color-ribbon-swirl-zd68lyivre9e0g2d.gif" alt="Rainbow Swirl" class="rainbow-footer-gif">
</div>