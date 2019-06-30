$(document).ready(function() {
    //Call plugins here
    $("#video-slider").owlCarousel();
});

$('.nav-link, .navbar-brand, .new-btn').click(function() {
    var sectionTo = $(this).attr('href');
    $('html, body').animate({
      scrollTop: $(sectionTo).offset().top
    }, 600);
});

// popovers Initialization
$(function () {
$('[data-toggle="popover"]').popover()
})