
/*document.write("Hello World ")
var a = prompt("Enter a information")
document.write(a)*/
    $('.home-slider').owlCarousel({
        items:1,
        nav:true,
        dots:false,
        autoplay:true,
        autoplayTimeout:4000,
        loop:true
    });

    $('.row').owlCarousel({
        items:2,
        nav:true,
        dots:false,
        autoplay:true,
        autoplayTimeout:4000,
        loop:true
    });
    
    $('.bestslider').owlCarousel({
        items:8,
        nav:true,
        dots:false,
        autoplay:true,
        autoplayTimeout:4000,
        loop:true
    });