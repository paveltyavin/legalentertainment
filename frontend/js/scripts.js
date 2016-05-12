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

  YMaps.jQuery(function () {
    var map = new YMaps.Map(YMaps.jQuery("#map")[0]);
    map.setCenter(new YMaps.GeoPoint(37.601244, 55.754299), 20);
    var placemark = new YMaps.Placemark(new YMaps.GeoPoint(37.601244, 55.754299));
    map.addOverlay(placemark);
  })

});



