---
layout: default
title: "hacker.md"
permalink: /hacker/
---

<style>
  body {
    background-image: url('https://i.pinimg.com/originals/8b/86/5d/8b865ddcb9bb441b73db346574214f49.gif');
    background-repeat: repeat;
    margin: 0;
  }
</style>


<style>
  .hacker-text {
    font-family: 'Courier New', monospace;
    color: #39FF14;
    text-align: center;
    text-shadow: 
      -1px -1px 0 #000,
      1px -1px 0 #000,
      -1px 1px 0 #000,
      1px 1px 0 #000;
  }

  /* Scale BOTH elements 3x their default sizes */
  .hacker-text.h1 {
    font-size: 3em; /* Default <h1> is ~2em, so this makes it ~6x normal text */
  }
  .hacker-text.p {
    font-size: 3em; /* Default <p> is 1em, so this triples it */
  }

  /* Container (unchanged) */
  .text-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
</style>

<div class="text-container">
  <h1 class="hacker-text h1">YOUR TITLE HERE</h1>  <!-- Now 3x larger than default <h1> -->
  <p class="hacker-text p">Your paragraph text, now 3x normal size.</p>  <!-- 3x default <p> -->
</div>