// Mobile Menu Functions
function openMenu() {
  const mobileMenu = document.querySelector('.mobile-menu');
  const overlay = document.querySelector('.mobile-menu-overlay');
  mobileMenu.classList.add('open');
  overlay.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeMenu() {
  const mobileMenu = document.querySelector('.mobile-menu');
  const overlay = document.querySelector('.mobile-menu-overlay');
  mobileMenu.classList.remove('open');
  overlay.classList.remove('open');
  document.body.style.overflow = '';
}

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', function() {
  // Close menu when clicking a menu item
  const menuItems = document.querySelectorAll('.mobile-menu .menu-item a');
  menuItems.forEach(item => {
    item.addEventListener('click', function(e) {
      // If it's an external link, let it navigate naturally
      if (this.href.startsWith('http') && !this.href.includes(window.location.hostname)) {
        return;
      }
      closeMenu();
    });
  });

  // Carousel Auto-rotation
  const slider = document.querySelector('#slider .slider-container');
  if (slider) {
    const slides = slider.querySelectorAll('.slide');
    const prevButton = document.querySelector('.slider-arrow--prev');
    const nextButton = document.querySelector('.slider-arrow--next');
    let currentSlide = 0;
    const delay = 5000;
    let slideInterval;

    const showSlide = (index) => {
      slides[currentSlide].classList.remove('active');
      currentSlide = index;
      slides[currentSlide].classList.add('active');
    };

    const nextSlide = () => showSlide((currentSlide + 1) % slides.length);
    const prevSlide = () => showSlide((currentSlide - 1 + slides.length) % slides.length);

    const startAutoRotation = () => {
      slideInterval = setInterval(nextSlide, delay);
    };

    const resetAutoRotation = () => {
      if (slideInterval) {
        clearInterval(slideInterval);
      }
      startAutoRotation();
    };

    if (slides.length > 0) {
      slides[0].classList.add('active');

      if (slides.length > 1) {
        startAutoRotation();
      }
    }

    if (nextButton) {
      nextButton.addEventListener('click', () => {
        nextSlide();
        resetAutoRotation();
      });
    }

    if (prevButton) {
      prevButton.addEventListener('click', () => {
        prevSlide();
        resetAutoRotation();
      });
    }
  }

  // Handle external links
  const links = document.querySelectorAll('a[href^="http"]');
  links.forEach(link => {
    if (!link.href.includes(window.location.hostname)) {
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener noreferrer');
    }
  });
});
