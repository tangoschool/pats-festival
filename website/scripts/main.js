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
    let currentSlide = 0;

    if (slides.length > 0) {
      slides[0].classList.add('active');

      if (slides.length > 1) {
        setInterval(function() {
          slides[currentSlide].classList.remove('active');
          currentSlide = (currentSlide + 1) % slides.length;
          slides[currentSlide].classList.add('active');
        }, 4000);
      }
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
