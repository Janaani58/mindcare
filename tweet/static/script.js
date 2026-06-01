// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Navbar active link update on scroll
window.addEventListener('scroll', () => {
    let current = '';
    const sections = document.querySelectorAll('section');
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (pageYOffset >= sectionTop - 60) {
            current = section.getAttribute('id');
        }
    });

    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href').slice(1) === current) {
            link.classList.add('active');
        }
    });
});

// Intersection Observer for fade-in animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeInUp 0.8s ease forwards';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.feature-card, .step').forEach(el => {
    observer.observe(el);
});

// Form submission with loading state
const form = document.querySelector('.analyze-form');
if (form) {
    form.addEventListener('submit', function(e) {
        const submitBtn = form.querySelector('button[type="submit"]');
        submitBtn.style.opacity = '0.7';
        submitBtn.style.pointerEvents = 'none';
    });
}

// Counter for character input
const textarea = document.querySelector('.emotion-textarea');
const charCounter = document.getElementById('char-counter');

if (textarea && charCounter) {
    textarea.addEventListener('input', function() {
        charCounter.textContent = this.value.length;
        if (this.value.length > 450) {
            charCounter.style.color = '#ff6b6b';
        } else if (this.value.length > 400) {
            charCounter.style.color = '#ffd700';
        } else {
            charCounter.style.color = '#999';
        }
    });
}

console.log('🧠 MindCare App Loaded Successfully!');
