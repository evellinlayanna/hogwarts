const $carrossel = document.querySelector(`.gliderjs`)

new Glider($carrossel, {
    slidesToShow: 'auto',
    slidesToScroll: 1,
    itemWidth: 211,
    draggable: true,
    arrows: {
        prev: "#esquerda",
        next: "#direita",
    },
    rewind: true,
    responsive: [
        {
            breakpoint: 1024,
            settings: {
                slidesToShow: 'auto',
                slidesToScroll: 'auto',
                itemWidth: 300,

            }
        }
    ]
})