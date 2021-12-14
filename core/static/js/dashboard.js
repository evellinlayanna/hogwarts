
const $slide = document.querySelector(`.slides`)

new Glider($slide, {
    slidesToShow: 1,
    slidesToScroll: 1,

    draggable: true,
    arrows: {
        prev: ".btn-slideE",
        next: ".btn-slideD",
    },
    rewind: true,
})