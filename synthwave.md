---
layout: synthwave
title: "Synthwave"
permalink: /synthwave/
---

<style>
  /* Song section styling for responsive layout */
  .song-section {
    display: flex;
    align-items: flex-start;
    margin-bottom: 40px;
    gap: 20px;
  }
  
  .media-container {
    flex-shrink: 0;
  }
  
  .text-container {
    flex-grow: 1;
  }
  
  /* Responsive layout - stack on mobile */
  @media screen and (max-width: 768px) {
    .song-section {
      flex-direction: column;
      align-items: center;
    }
    
    .media-container {
      margin-bottom: 15px;
    }
    
    .text-container p {
      text-align: center;
    }
  }
</style>

# Test
