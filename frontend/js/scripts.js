$(function () {

  $(".subscriber .section .item > a").click(function () {
    $(this).parent(".item").find('.content').fadeIn(300)
  });
  $(".subscriber .content .remove").click(function () {
    $(this).parents('.content').fadeOut(300)
  });

  $(".mainMenu ul li a").click(function () {
    var div = $(this).attr("href");
    $("html, body").animate({scrollTop: $(div).offset().top - 102}, '500');
    return false;
  });

  $(window).scroll(function () {
    var left = $(window).scrollLeft();
    $('header').css({left: -left});
  });

  $('.lang .btn').click(function () {
    var lang = $(this).data('lang');
    $('[name=language]').val(lang);
    $('form.set_language_form').submit();
  });

  ymaps.ready(function () {
    var map = new ymaps.Map("map", {
      center: [55.7543, 37.6012],
      zoom: 17
    });
    var placemark = new ymaps.Placemark([55.7543, 37.6012], {
      hintContent: 'Никитская 8а',
      balloonContent: 'Никитская 8а'
    });

    map.geoObjects.add(placemark);
    
  });
});



