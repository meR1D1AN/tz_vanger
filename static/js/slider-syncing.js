$(document).ready(function(){
  $('.slider-main').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: false,
      fade: true,
      asNavFor: '.slider-nav'
  });
  $('.slider-nav').slick({
      slidesToShow: 5,
      slidesToScroll: 1,
      asNavFor: '.slider-main',
      dots: false,
      centerMode: true,
      focusOnSelect: true,
      arrows: true,
      prevArrow: '<button type="button" class="slick-prev"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="48" height="48" rx="24" fill="#FF342B"/><path d="M18 20L14 24L18 28" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M14 24H34" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>',
      nextArrow: '<button type="button" class="slick-next"><svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="48" height="48" rx="24" fill="#FF342B"/><path d="M30 20L34 24L30 28" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 24H14" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>',
      responsive: [
          {
              breakpoint: 768,
              settings: {
                  slidesToShow: 3,
                  arrows: false
              }
          }
      ]
  });
  Fancybox.bind("[data-fancybox]");
});