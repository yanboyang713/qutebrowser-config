// ==UserScript==
// @name Skip YouTube ads
// @description Skips the ads in YouTube videos
// @run-at document-start
// @include *.youtube.com/*
// ==/UserScript==

document.addEventListener('load', () => {
  const defined = v => v !== null && v !== undefined;
  const timeout = setInterval(() => {
    const skipBtn = document.querySelector('.videoAdUiSkipButton,.ytp-ad-skip-button');
    const ad = [...document.querySelectorAll('.ad-showing')][0];
    const sidAd = document.querySelector('ytd-action-companion-ad-renderer');
    const displayAd = document.querySelector('div#root.style-scope.ytd-display-ad-renderer.yt-simple-endpoint');
    const sparklesContainer = document.querySelector('div#sparkles-container.style-scope.ytd-promoted-sparkles-web-renderer');
    const mainContainer = document.querySelector('div#main-container.style-scope.ytd-promoted-video-renderer');
    const feedAd = document.querySelector('ytd-in-feed-ad-layout-renderer');
    const mastheadAd = document.querySelector('.ytd-video-masthead-ad-v3-renderer');
    const sponsor = document.querySelectorAll("div#player-ads.style-scope.ytd-watch-flexy, div#panels.style-scope.ytd-watch-flexy");
    const nonVid = document.querySelector(".ytp-ad-skip-button-modern");

    if (ad)
    {
        const video = document.querySelector('video');
        video.playbackRate = 10;
        video.volume = 0;
        video.currentTime = isFinite(video.duration)? video.duration : 0; // handles NaN video duration
        skipBtn?.click();
    }

    sidAd?.remove();
    displayAd?.remove();
    sparklesContainer?.remove();
    mainContainer?.remove();
    feedAd?.remove();
    mastheadAd?.remove();
    sponsor?.forEach((element) => {
         if (element.getAttribute("id") === "panels") {
            element.childNodes?.forEach((childElement) => {
              if (childElement.data?.targetId && childElement.data.targetId !=="engagement-panel-macro-markers-description-chapters")
                  //Skipping the Chapters section
                    childElement.remove();
                  });
               } else {
                   element.remove();
               }
     });
    nonVid?.click();
  }, 50);
  return function() {
      clearTimeout(timeout);
  }
}, true);
