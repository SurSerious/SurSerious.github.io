---
layout: default
title: chatbot.md
permalink: /chatbot/
---

<div class="gradio-container">
  <gradio-app
    src="https://sureserious-advanced-chatbot.hf.space"
    class="responsive-gradio"
  ></gradio-app>
</div>

<style>
  /* Mobile-first container */
  .gradio-container {
    display: flex;
    justify-content: center;
    margin: 0 auto;
    padding: 1rem;
    max-width: 100%;
    min-height: 60vh; /* Ensures space while loading */
  }

  /* Gradio-specific responsiveness */
  .responsive-gradio {
    width: 100%;
    height: 100%;
    min-height: 500px; /* Default height */
    border: none;
    border-radius: 12px;
    overflow: hidden; /* Prevents inner scrollbars */
  }

  /* Mobile adjustments */
  @media (max-width: 768px) {
    .responsive-gradio {
      min-height: 400px;
    }
    .gradio-container {
      padding: 0.5rem;
    }
  }

  /* Tiny screens */
  @media (max-width: 480px) {
    .responsive-gradio {
      min-height: 350px;
      border-radius: 8px;
    }
  }
</style>

<script
  type="module"
  src="https://gradio.s3-us-west-2.amazonaws.com/5.0.1/gradio.js"
></script>
