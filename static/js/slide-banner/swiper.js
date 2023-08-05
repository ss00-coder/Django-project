
var swiper = new Swiper(".mySwiper", {
  slidesPerView: 3,
  spaceBetween: 10,
  centeredSlides: true,
  loop: true,

  autoplay: {
    delay: 4000,
  },

  pagination: {
    el: ".slide-banner-count",
    type: "fraction",

    formatFractionCurrent: function (number) {
      switch(number) {
        case 1:
          return number;

        case 2:
          return number;

        case 3:
          return number;

        case 4:
          return number;

        case 5:
          return number = 1;

        case 6:
          return number = 2;

        case 7:
          return number = 3;

        case 8:
          return number = 4;
      }
    },
    formatFractionTotal: function (number) {
      return number-4;
    },

    renderFraction: function (currentClass, totalClass) {
      return '<span class="' + currentClass + '"></span>'
      + "<span style='color: hsla(0,0%,100%,.8); font-weight: 400; font-size: 13px; line-height: 18px; margin-left: 2px'>/</span>"
      + '<span class="' + totalClass + '"></span>';
    }
  },

  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});





