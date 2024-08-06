function updateCarouselPosition(carouselClass, currentIndex, cardWidth) {
    const carousel = document.querySelector(`.${carouselClass}`);
    const newTransformValue = `translateX(-${currentIndex * cardWidth}px)`;
    carousel.style.transform = newTransformValue;
  }
  
  function scrollLeftt(carouselClass) {
    const cards = document.querySelectorAll(`.${carouselClass} .card-visiter`);
    const cardWidth = cards[0].offsetWidth + 20; // Width of each card + margin
    let currentIndex = getCurrentIndex(carouselClass);
    
    if (currentIndex > 0) {
      currentIndex--;
      updateCarouselPosition(carouselClass, currentIndex, cardWidth);
      updateCurrentIndex(carouselClass, currentIndex);
    }
  }
  
  function scrollRight(carouselClass) {
    const cards = document.querySelectorAll(`.${carouselClass} .card-visiter`);
    const cardWidth = cards[0].offsetWidth + 20; // Width of each card + margin
    let currentIndex = getCurrentIndex(carouselClass);
    
    if (currentIndex < cards.length - 1) {
      currentIndex++;
      updateCarouselPosition(carouselClass, currentIndex, cardWidth);
      updateCurrentIndex(carouselClass, currentIndex);
    }
  }
  
  function getCurrentIndex(carouselClass) {
    return parseInt(document.querySelector(`.${carouselClass}`).getAttribute('data-current-index')) || 0;
  }
  
  function updateCurrentIndex(carouselClass, currentIndex) {
    document.querySelector(`.${carouselClass}`).setAttribute('data-current-index', currentIndex);
  }
  