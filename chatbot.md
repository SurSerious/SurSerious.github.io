---
layout: chatbot
title: chatbot.md
permalink: /chatbot/
---

<div class="chatbot-container">
  <iframe
    src="https://sureserious-advanced-chatbot.hf.space"
    frameborder="0"
    class="responsive-iframe"
  ></iframe>
</div>

<style>
  /* Mobile-first responsive container */
  .chatbot-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0 auto;
    padding: 20px;
    max-width: 100%;
  }

  /* Responsive iframe */
  .responsive-iframe {
    width: 100%;
    height: 500px;  /* Default height for desktop */
    border: none;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }

  /* Mobile adjustments */
  @media (max-width: 768px) {
    .responsive-iframe {
      height: 400px;
    }
    .chatbot-container {
      padding: 10px;
    }
  }

  /* Small phones */
  @media (max-width: 480px) {
    .responsive-iframe {
      height: 350px;
    }
  }
</style>