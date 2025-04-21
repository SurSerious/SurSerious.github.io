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

  .rainbow-gif-container {
    text-align: center;
    margin: 0 auto 30px auto;
  }

  .rainbow-gif {
    width: 175px;
    height: auto;
  }
  
  /* Footer rainbow GIF styling */
  .footer-rainbow {
    width: 100%;
    display: block;
    margin-top: 50px; /* Space above the footer */
  }
  
  /* Add some minimum content height to ensure scrolling */
  .content-wrapper {
    min-height: 100vh; /* Makes content at least full viewport height */
  }
</style>

<div class="content-wrapper">
  <h1 class="rainbow-title">Neon Dreams Only A Moment Away</h1>

  <div class="rainbow-gif-container">
    <img src="https://gifdb.com/images/high/rainbow-color-ribbon-swirl-zd68lyivre9e0g2d.gif" alt="Rainbow Swirl" class="rainbow-gif">
  </div>

  <p>This is your neon-themed page content. The rainbow GIF is centered below the title.</p>
  
  <!-- Add more content here to ensure scrolling -->
  <div style="height: 800px;">
    <!-- Placeholder space to ensure scrolling is needed -->
    <p>Additional content can go here...</p>
  </div>
  
  <!-- Full-width rainbow GIF at the bottom -->
  <img src="https://gifdb.com/images/high/rainbow-color-fiber-spectrum-akrpawy99rt68bn9.gif" alt="Rainbow Fiber Spectrum" class="footer-rainbow">
</div>