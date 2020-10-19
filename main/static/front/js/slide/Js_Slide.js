$('.play-button').on('click', function() {

    $(this).play();
});

$('.slider-video').on('play', function() {
    $(this).attr('controls', );
});

// Additionnal code for the slider
var pos = 0,
    slides = $('.slide'),
    numOfSlides = slides.length;

function nextSlide() {
    stopCurrentVideo();
    slides.eq(pos).animate({ left: '-100%' }, 500);
    pos = pos >= numOfSlides - 1 ? 0 : ++pos;
    slides.eq(pos).css({ left: '100%' }).animate({ left: 0 }, 500);
}

function previousSlide() {
    stopCurrentVideo();
    slides.eq(pos).animate({ left: '100%' }, 500);
    pos = pos == 0 ? numOfSlides - 1 : --pos;
    slides.eq(pos).css({ left: '-100%' }).animate({ left: 0 }, 500);
}

function stopCurrentVideo() {
    $('.slider-video:eq(' + pos + ')').load().removeAttr('controls')
        .siblings('.overlay-content').show().find('.play-button').show();
}

$('.left').click(previousSlide);
$('.right').click(nextSlide);