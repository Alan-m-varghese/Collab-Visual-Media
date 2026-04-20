document.addEventListener('DOMContentLoaded', () => {
    // 1. Scroll animations (Intersection Observer)
    const fadeElements = document.querySelectorAll('.fade-in');
    
    const fadeObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Optional: stop observing once faded in
                // fadeObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    fadeElements.forEach(el => fadeObserver.observe(el));

    // 2. Navbar Background on Scroll
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 3. Accordion Interaction & Image Swap for Services
    const accordionItems = document.querySelectorAll('.accordion-item');
    const serviceImage = document.getElementById('service-image');

    accordionItems.forEach(item => {
        item.addEventListener('click', () => {
            // Remove active class from all
            accordionItems.forEach(acc => acc.classList.remove('active'));
            // Add active class to clicked
            item.classList.add('active');

            // Swap image with fade effect
            const newImageSrc = item.getAttribute('data-image');
            serviceImage.style.opacity = 0;
            
            setTimeout(() => {
                serviceImage.src = 'assets/images/' + newImageSrc;
                serviceImage.style.opacity = 1;
            }, 300); // Wait for fade out to complete
        });
    });

    // 4. Mobile Menu Toggle (Basic implementation)
    const mobileToggle = document.querySelector('.mobile-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (mobileToggle) {
        mobileToggle.addEventListener('click', () => {
            // Very simple inline style toggle for mobile menu demo
            // In a production app, you'd toggle a CSS class and handle animations
            if (navLinks.style.display === 'flex') {
                navLinks.style.display = 'none';
            } else {
                navLinks.style.display = 'flex';
                navLinks.style.flexDirection = 'column';
                navLinks.style.position = 'absolute';
                navLinks.style.top = '100%';
                navLinks.style.left = '0';
                navLinks.style.width = '100%';
                navLinks.style.background = '#0f1011';
                navLinks.style.padding = '1rem';
            }
        });
    }

    // Trigger initial scroll event to set navbar state
    window.dispatchEvent(new Event('scroll'));
});
