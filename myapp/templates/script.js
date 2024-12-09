let currentIndex = 0;

function moveSlide(direction) {
    const slides = document.querySelectorAll('.carousel-item');
    const totalSlides = slides.length;
    
    currentIndex += direction;

    // Se o índice for menor que 0, volta para a última imagem
    if (currentIndex < 0) {
        currentIndex = totalSlides - 1;
    }

    // Se o índice for maior que o número de slides, vai para o primeiro slide
    if (currentIndex >= totalSlides) {
        currentIndex = 0;
    }

    // Atualiza a posição das imagens no carrossel
    const carousel = document.querySelector('.carousel');
    carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
}
