document.addEventListener('DOMContentLoaded', () => {

    /* ─────────────────────────────────────────────
       1. Smooth Scroll — enhanced easing via JS
    ───────────────────────────────────────────── */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const target = document.querySelector(anchor.getAttribute('href'));
            if (!target) return;
            e.preventDefault();

            // Close mobile menu if open
            closeMenu();

            const offset  = 90;
            const top     = target.getBoundingClientRect().top + window.scrollY - offset;
            const start   = window.scrollY;
            const distance = top - start;
            const duration = 900;
            let startTime = null;

            function easeInOutQuart(t) {
                return t < 0.5 ? 8 * t * t * t * t : 1 - Math.pow(-2 * t + 2, 4) / 2;
            }

            function step(timestamp) {
                if (!startTime) startTime = timestamp;
                const elapsed  = timestamp - startTime;
                const progress = Math.min(elapsed / duration, 1);
                window.scrollTo(0, start + distance * easeInOutQuart(progress));
                if (progress < 1) requestAnimationFrame(step);
            }
            requestAnimationFrame(step);
        });
    });


    /* ─────────────────────────────────────────────
       2. Scroll-triggered Fade-in Animations
    ───────────────────────────────────────────── */
    const fadeEls = document.querySelectorAll('.fade-in, .fade-in-left');

    const fadeObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.08,
        rootMargin: '0px 0px -60px 0px'
    });

    fadeEls.forEach(el => fadeObserver.observe(el));


    /* ─────────────────────────────────────────────
       3. Navbar: compact on scroll + slight tint
    ───────────────────────────────────────────── */
    const navbar = document.querySelector('.navbar');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const current = window.scrollY;
        if (current > 60) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        lastScroll = current;
    }, { passive: true });

    window.dispatchEvent(new Event('scroll'));


    /* ─────────────────────────────────────────────
       4. Accordion + Image Swap (Services)
    ───────────────────────────────────────────── */
    const accordionItems = document.querySelectorAll('.accordion-item');
    const serviceImage   = document.getElementById('service-image');

    accordionItems.forEach(item => {
        item.addEventListener('click', () => {
            accordionItems.forEach(acc => acc.classList.remove('active'));
            item.classList.add('active');

            const newSrc = 'assets/images/' + item.getAttribute('data-image');
            serviceImage.style.opacity = '0';
            serviceImage.style.transform = 'scale(0.97)';

            setTimeout(() => {
                serviceImage.src = newSrc;
                serviceImage.style.opacity  = '1';
                serviceImage.style.transform = 'scale(1)';
            }, 320);
        });
    });


    /* ─────────────────────────────────────────────
       5. Mobile Menu — class-based, backdrop, close
    ───────────────────────────────────────────── */
    const mobileToggle = document.querySelector('.mobile-toggle');
    const navLinks     = document.querySelector('.nav-links');
    const toggleIcon   = mobileToggle ? mobileToggle.querySelector('i') : null;

    // Create backdrop element and append to body
    const backdrop = document.createElement('div');
    backdrop.className = 'menu-backdrop';
    document.body.appendChild(backdrop);

    function openMenu() {
        navLinks.classList.add('active');
        mobileToggle.classList.add('open');
        backdrop.classList.add('active');
        document.body.style.overflow = 'hidden';
        if (toggleIcon) {
            toggleIcon.className = 'ph ph-x';  // change to X icon
        }
    }

    function closeMenu() {
        navLinks.classList.remove('active');
        mobileToggle.classList.remove('open');
        backdrop.classList.remove('active');
        document.body.style.overflow = '';
        if (toggleIcon) {
            toggleIcon.className = 'ph ph-list';  // restore hamburger
        }
    }

    if (mobileToggle) {
        mobileToggle.addEventListener('click', () => {
            if (navLinks.classList.contains('active')) {
                closeMenu();
            } else {
                openMenu();
            }
        });
    }

    // Close on backdrop click
    backdrop.addEventListener('click', closeMenu);

    // Close on Escape
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeMenu();
    });

    /* Inject CTA button + social icons into mobile menu if not already there */
    if (!navLinks.querySelector('.nav-cta-btn')) {
        const ctaBtn = document.createElement('a');
        ctaBtn.href = '#contact';
        ctaBtn.className = 'nav-cta-btn';
        ctaBtn.textContent = "Let's Talk";
        navLinks.appendChild(ctaBtn);
    }

    if (!navLinks.querySelector('.nav-social')) {
        const socials = document.createElement('div');
        socials.className = 'nav-social';
        socials.innerHTML = `
            <a href="#" aria-label="Instagram"><i class="ph-fill ph-instagram-logo"></i></a>
            <a href="#" aria-label="Facebook"><i class="ph-fill ph-facebook-logo"></i></a>
            <a href="#" aria-label="LinkedIn"><i class="ph-fill ph-linkedin-logo"></i></a>
        `;
        navLinks.appendChild(socials);
    }


    /* ─────────────────────────────────────────────
       6. Parallax micro-effect on hero card
    ───────────────────────────────────────────── */
    const heroCard = document.querySelector('.hero-card');
    if (heroCard) {
        document.addEventListener('mousemove', (e) => {
            if (window.innerWidth < 1024) return;
            const cx = window.innerWidth  / 2;
            const cy = window.innerHeight / 2;
            const dx = (e.clientX - cx) / cx;
            const dy = (e.clientY - cy) / cy;
            heroCard.style.transform = `perspective(1200px) rotateY(${dx * 1.5}deg) rotateX(${-dy * 1.5}deg)`;
        });
        document.addEventListener('mouseleave', () => {
            heroCard.style.transform = 'perspective(1200px) rotateY(0) rotateX(0)';
        });
    }


    /* ─────────────────────────────────────────────
       7. Stat counters — count-up on scroll
    ───────────────────────────────────────────── */
    const statItems = document.querySelectorAll('.stat-item h3');

    const countObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('counted');
                countObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    statItems.forEach(el => countObserver.observe(el));

});
