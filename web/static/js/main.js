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
    // Navbar mobile
    $(".btn-mobile").click(function (e) { 
        e.preventDefault();
        $(".navbar-mobile").toggleClass('display');
    });

    // Navbar State
    $('.links a').on('click', function() {

        var scrollAnchor = $(this).attr('data-scroll'),
            scrollPoint = $('section[data-anchor="' + scrollAnchor + '"]').offset().top - 28;
    
        $('body,html').animate({
            scrollTop: scrollPoint
        }, 500);
    
        return false;
    
    })
    
    
    $(window).scroll(function() {
        var windscroll = $(window).scrollTop();
        if (windscroll >= 100) {
            $('.links').addClass('fixed');
            $('section').each(function(i) {
                if ($(this).position().top <= windscroll - 20) {
                    $('.links a.active').removeClass('active');
                    $('.links a').eq(i).addClass('active');
                }
            });
    
        } else {
    
            $('nav').removeClass('fixed');
            $('nav a.active').removeClass('active');
            $('nav a:first').addClass('active');
        }
    
    }).scroll();

});