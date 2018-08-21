(function () {
    // Phone mask
    $(document).ready(function () {
        $('.phone-mask').mask('+7 (000) 000-00-00');

    });

    // Tabs menu
    document.addEventListener('click', function (e) {

        // Табы меню
        if (e.target.closest('.section-3__categories-item')) {
            e.target.parentElement.querySelector('.section-3__categories-item.active').classList.remove('active');
            e.target.closest('.section-3__categories-item').classList.toggle('active');

            var indexTab = $(e.target.closest('.section-3__categories')).find('.active').index();

            $(e.target.closest('.container')).find($('.section-3__menu.active')).removeClass('active');
            console.log($(e.target.closest('.container')).find($('.section-3__menu'))[indexTab].classList.add('active'));
        }

        // Само меню
        if (e.target.closest('.section-3__nav-item')) {
            e.target.parentElement.querySelector('.section-3__nav-item_active').classList.remove('section-3__nav-item_active');
            e.target.closest('.section-3__nav-item').classList.toggle('section-3__nav-item_active');

            var indexNav = $(e.target.closest('.container')).find('.section-3__nav-item_active').index();

            $(e.target.closest('.container')).find($('.section-3__block_active')).removeClass('section-3__block_active');
            console.log($(e.target.closest('.container')).find($('.section-3__block'))[indexNav].classList.add('section-3__block_active'));
        }
    });

    // Anchors
    $(document).ready(function () {
        $("a.anchor-link").click(function () {
            var elementClick = $(this).attr("href");
            var destination = $(elementClick).offset().top;

            jQuery("html:not(:animated),body:not(:animated)").animate({
                scrollTop: elementClick !== '#main' ? destination - 72 : destination
            }, 800);
            return false;
        });
    });

    // Popup
    $('.close-popup').click(function () {
        $('.popup').hide(100);
    });

    $(document).keyup(function (e) {
        if (e.keyCode == 27) { // escape key maps to keycode '27'
            $('.popup').hide(100);
        }
    });

    $('.show-popup').click(function (e) {
        e.preventDefault();

        $('.popup').show(100);
        $($('.popup__radio')[0]).find('.popup__radio-input').prop("checked", true);
    });

    // Carousel
    $(document).ready(function () {
        $('.carousel').imagesLoaded(function () {
            $('.owl-carousel').owlCarousel({
                dots: false,
                margin: 15,
                center: true,
                loop: true,
                nav: true,
                navText: '<>',
                navElement: 'div',
                autoWidth: true,
                lazyLoad: true
            });
        });
    });

    // Lightbox
    lightbox.option({
        'fadeDuration': 300,
        'imageFadeDuration': 300,
        'resizeDuration': 300,
        'wrapAround': true
    });

    // Top nav fixed
    var toggleNav = function () {
        if (window.pageYOffset >= 100) {
            $('.header').addClass('header_fixed');
        }
        else {
            $('.header').removeClass('header_fixed');
        }
    };
    toggleNav();
    $(window).scroll(function (e) {
        toggleNav();
    });

    $(`.send-form`).submit(function(e) {
        e.preventDefault(); // avoid to execute the actual submit of the form.

        var form = $(this);
        var url = form.attr('action');
        var formData = form.serialize();
        // console.log(form.children(`input[name="name"]`));

        $.ajax({
               type: "POST",
               url: url,
               data: formData, // serializes the form's elements.
               success: function(data)
               {
                   console.log(data); // show response from the php script.
               }
             });
    });
})();