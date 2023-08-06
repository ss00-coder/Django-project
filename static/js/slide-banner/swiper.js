
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
      switch (number) {
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
      return number - 4;
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

var subswiper = new Swiper('.subSwiper', {
  slidesPerView: 5,
  spaceBetween: 10,

  navigation: {
    nextEl: ".swiper-sub-button-next",
    prevEl: ".swiper-sub-button-prev",
  },

  on: {
    slideChange: function () {
      this.realIndex <= 0 ? $('.swiper-sub-button-prev').hide() : $('.swiper-sub-button-prev').css('display','flex');
      this.realIndex >= 10 ? $('.swiper-sub-button-next').hide() : $('.swiper-sub-button-next').css('display','flex');
    }
  }
});

var thirdswiper = new Swiper('.thirdSwiper', {
  slidesPerView: 5,
  spaceBetween: 10,

  navigation: {
    nextEl: ".swiper-third-button-next",
    prevEl: ".swiper-third-button-prev",
  },

  on: {
    slideChange: function () {
      this.realIndex <= 0 ? $('.swiper-third-button-prev').hide() : $('.swiper-third-button-prev').css('display','flex');
      this.realIndex >= 10 ? $('.swiper-third-button-next').hide() : $('.swiper-third-button-next').css('display','flex');
    }
  }
});

var fourthswiper = new Swiper('.fourthSwiper', {
  slidesPerView: 5,
  spaceBetween: 10,

  navigation: {
    nextEl: ".swiper-fourth-button-next",
    prevEl: ".swiper-fourth-button-prev",
  },

  on: {
    slideChange: function () {
      this.realIndex <= 0 ? $('.swiper-fourth-button-prev').hide() : $('.swiper-fourth-button-prev').css('display','flex');
      this.realIndex >= 10 ? $('.swiper-fourth-button-next').hide() : $('.swiper-fourth-button-next').css('display','flex');
    }
  }
});



let subCount = 0;
let thirdCount = 0;
let fourthCount = 0;

$('.swiper-sub-button-prev').on('click', () => {
  subswiper.slideTo(subCount -=5 ,400,false)
})

$('.swiper-sub-button-next').on('click', () => {
  subswiper.slideTo(subCount +=5 ,400,false)
})


$('.swiper-third-button-prev').on('click', () => {
  thirdswiper.slideTo(thirdCount -=5 ,400,false)
})

$('.swiper-third-button-next').on('click', () => {
  thirdswiper.slideTo(thirdCount +=5 ,400,false)
})

$('.swiper-fourth-button-prev').on('click', () => {
  fourthswiper.slideTo(fourthCount -=5 ,400,false)
})

$('.swiper-fourth-button-next').on('click', () => {
  fourthswiper.slideTo(fourthCount +=5 ,400,false)
})











