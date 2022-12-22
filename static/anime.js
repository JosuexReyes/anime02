const audio = document.getElementById("backgroundMusic");


   const audioQuery = document.querySelector("audio");
   window.addEventListener("DOMContentLoaded", event => {

       audioQuery.volume = 1;
       audioQuery.play();
   });

   function audioController() {
      if (!audio.paused) {
           audio.pause();
       }
      else {
          audio.play();
      }
   }

   imageTracker = "i"
   function imageChange() {
       var image = document.getElementById("audioController");


       if (imageTracker == "i"){
           image.src = "https://user-images.githubusercontent.com/111708286/205412321-5cb7411d-3074-40ce-a0ee-e2d529ba2a89.png"
           imageTracker = "I"
       }
       else {
           image.src = "https://user-images.githubusercontent.com/111708286/205412302-8c2836bb-11c1-4ae6-87b6-f7226075b959.png"
           imageTracker = "i"
       }
   }

   const menuBtn = document.querySelector('.menuHamburger')
   let menuOpen = false;
   menuBtn.addEventListener('click', () => {
       if(!menuOpen) {
           menuBtn.classList.add('open');
           menuOpen = true;
       } else {
           menuBtn.classList.remove('open');
           menuOpen = false;
       }
   });
   const list = document.querySelector('.rightBarStuff');
menuBtn.addEventListener('click', () => {
    list.classList.toggle('show');
});

const qq = document.querySelector(".dropdownContent");
function s() {
        qq.style.display = "flex";
  }

  function c() {
        qq.style.display = "none";
}

function showOrHide() {
    if (qq.style.display === "none") {
      s()
    } else {
      c()
    }
  }