$(document).ready(function () {
    // sticky navigation menu

    let nav_offset_top = $('.navbar').height() + 50;

    function navbarFixed() {
        if ($('#nav').length) {
            $(window).scroll(function () {
                let scroll = $(window).scrollTop();
                if (scroll >= nav_offset_top) {
                    $('#nav').addClass('active');
                } else {
                    $('#nav').removeClass('active');
                }
            })
        }
    }

    navbarFixed();

});