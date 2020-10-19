(function($) {
	"use strict"
	
	$(window).on('scroll', function() {
		// Back to top appear
		wScroll > 740 ? $('#back-to-top').addClass('active') : $('#back-to-top').removeClass('active')
	});
	
	// Back to top
	$('#back-to-top').on("click", function(){
		$('body,html').animate({
            scrollTop: 0
        }, 500);
	});
	

	// Owl Carousel
	$('#owl-carousel-1').owlCarousel({
		loop:true,
		margin:4,
		dots : false,
		nav: false,autoplay : true,
		responsive:{
			0:{
				items:1
			},
			768:{
				items:2
			},
			992:{
				items:2
			},
			992:{
				items:2
			},
		}
	});
	
})(jQuery);