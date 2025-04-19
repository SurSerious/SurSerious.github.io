---
layout: default
title: "classical.md"
permalink: /classical/
---

<style>
  html, body {
    margin: 0;
    padding: 0;
    height: 100%;
  }

  .music-bg {
    background-image: url('/assets/images/musicbackground.jpeg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    min-height: 100vh;
    width: 100%;
    margin: 0;
    padding: 2rem 1rem;
    box-sizing: border-box;
    color: white;
    text-align: center;
  }

  .video-container {
    margin-top: 2rem;
    max-width: 640px;
    margin-left: auto;
    margin-right: auto;
  }

  wistia-player {
    width: 100%;
    height: 360px;
    display: block;
  }
</style>

<div class="music-bg">
  <h1 style="margin-top: 0;">Welcome to the Music Page</h1>

  <div class="video-container">
    <script src="https://fast.wistia.com/player.js" async></script>
    <script src="https://fast.wistia.com/embed/kj3p97uwee.js" async type="module"></script>
    <style>
      wistia-player[media-id='kj3p97uwee']:not(:defined) {
        background: center / cover no-repeat url('https://fast.wistia.com/embed/medias/kj3p97uwee/swatch');
        display: block;
        filter: blur(5px);
        padding-top: 56.25%;
      }
    </style>
    <wistia-player media-id="kj3p97uwee" aspect="16:9"></wistia-player>
  </div>
</div>
