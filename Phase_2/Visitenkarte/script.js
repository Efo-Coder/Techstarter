// ============================================
// THEME TOGGLE MIT JAVASCRIPT-HOVER-EFFEKTEN
// ============================================

function initThemeToggle() {
    const themeButton = document.querySelector('.theme-toggle');
    
    if (!themeButton) return;
    
    // Hover-Effekte per JavaScript
    themeButton.addEventListener('mouseenter', function() {
        this.style.background = 'rgba(255, 255, 255, 0.2)';
        this.style.borderColor = 'var(--accent-color)';
        this.style.color = 'var(--accent-color)';
        this.style.boxShadow = '0 12px 35px var(--shadow-color)';
    });
    
    themeButton.addEventListener('mouseleave', function() {
        this.style.background = 'var(--glass-bg)';
        this.style.borderColor = 'var(--glass-border)';
        this.style.color = 'var(--text-primary)';
        this.style.boxShadow = '0 8px 25px var(--shadow-color)';
    });
    
    // Click-Feedback
    themeButton.addEventListener('mousedown', function() {
        this.style.background = 'rgba(255, 255, 255, 0.3)';
        this.style.boxShadow = '0 6px 20px var(--shadow-color)';
    });
    
    themeButton.addEventListener('mouseup', function() {
        this.style.background = 'rgba(255, 255, 255, 0.2)';
        this.style.boxShadow = '0 12px 35px var(--shadow-color)';
    });
    
    // Touch-Events für Mobile
    themeButton.addEventListener('touchstart', function() {
        this.style.background = 'rgba(255, 255, 255, 0.3)';
    });

    themeButton.addEventListener('touchend', function() {
        this.style.background = 'var(--glass-bg)';
    });
}

// ============================================
// ERWEITERTE THEME MANAGEMENT FUNKTION
// ============================================

const themes = ['default', 'purple', 'green', 'sunset'];
let currentThemeIndex = 0;

function toggleTheme() {
    const themeButton = document.querySelector('.theme-toggle');
    
    // Visual Click-Feedback ohne Movement
    themeButton.style.background = 'var(--accent-color)';
    themeButton.style.color = 'white';
    
    setTimeout(() => {
        currentThemeIndex = (currentThemeIndex + 1) % themes.length;
        const newTheme = themes[currentThemeIndex];
        
        if (newTheme === 'default') {
            document.documentElement.removeAttribute('data-theme');
        } else {
            document.documentElement.setAttribute('data-theme', newTheme);
        }
        
        // Theme-Wechsel Animation
        document.body.style.transition = 'all 0.5s ease';
        setTimeout(() => {
            document.body.style.transition = '';
        }, 500);
        
        // Save theme preference
        localStorage.setItem('preferred-theme', newTheme);
        
        // Button zurücksetzen nach Animation
        setTimeout(() => {
            themeButton.style.background = 'rgba(255, 255, 255, 0.2)';
            themeButton.style.color = 'var(--accent-color)';
        }, 200);
        
    }, 100);
}

// Load saved theme on page load
function loadSavedTheme() {
    const savedTheme = localStorage.getItem('preferred-theme');
    if (savedTheme && savedTheme !== 'default') {
        document.documentElement.setAttribute('data-theme', savedTheme);
        currentThemeIndex = themes.indexOf(savedTheme);
    }
}

// ============================================
// TYPING ANIMATION - IT-SPEZIFISCH ERWEITERT
// ============================================

const typingText = document.querySelector('.typing-text');
const phrases = [
    'Full-Stack Developer',
    'DevOps Engineer', 
    'Cloud Architect',
    'System Administrator',
    'Code Reviewer',
    'Tech Lead',
    'Software Engineer',
    'Database Designer'
];

let phraseIndex = 0;
let charIndex = 0;
let isDeleting = false;
let typingSpeed = 100;

function typeWriter() {
    const currentPhrase = phrases[phraseIndex];
    
    if (isDeleting) {
        typingText.textContent = currentPhrase.substring(0, charIndex - 1);
        charIndex--;
        typingSpeed = 50;
    } else {
        typingText.textContent = currentPhrase.substring(0, charIndex + 1);
        charIndex++;
        typingSpeed = 100;
    }
    
    if (!isDeleting && charIndex === currentPhrase.length) {
        // Pause at end of phrase
        typingSpeed = 2000;
        isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        typingSpeed = 500;
    }
    
    setTimeout(typeWriter, typingSpeed);
}

// ============================================
// COUNTER ANIMATION
// ============================================

function animateCounters() {
    const counters = document.querySelectorAll('.stat-number');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = parseInt(counter.getAttribute('data-target'));
                const duration = 2000; // 2 seconds
                const increment = target / (duration / 16); // 60fps
                let current = 0;
                
                const updateCounter = () => {
                    current += increment;
                    if (current < target) {
                        counter.textContent = Math.floor(current);
                        requestAnimationFrame(updateCounter);
                    } else {
                        counter.textContent = target;
                    }
                };
                
                updateCounter();
                observer.unobserve(counter);
            }
        });
    }, { threshold: 0.5 });
    
    counters.forEach(counter => observer.observe(counter));
}

// ============================================
// SMOOTH CARD ENTRANCE ANIMATION
// ============================================

function initCardAnimation() {
    const card = document.querySelector('.business-card');
    const sections = card.querySelectorAll('.profile-section, .skills-section, .contact-section, .social-section, .stats-section');
    
    // Add entrance animation to sections
    sections.forEach((section, index) => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(30px)';
        section.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
        
        setTimeout(() => {
            section.style.opacity = '1';
            section.style.transform = 'translateY(0)';
        }, 200 + (index * 150));
    });
}

// ============================================
// PARTICLE SYSTEM ENHANCEMENT
// ============================================

function createAdvancedParticles() {
    const particleContainer = document.querySelector('.particle-container');
    const particleCount = 15;
    
    // Clear existing particles
    particleContainer.innerHTML = '';
    
    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        
        // Random positioning and properties
        const startX = Math.random() * window.innerWidth;
        const startY = window.innerHeight + 50;
        const size = Math.random() * 4 + 2;
        const duration = Math.random() * 10 + 15;
        const delay = Math.random() * 5;
        
        particle.style.left = startX + 'px';
        particle.style.top = startY + 'px';
        particle.style.width = size + 'px';
        particle.style.height = size + 'px';
        particle.style.animationDuration = duration + 's';
        particle.style.animationDelay = '-' + delay + 's';
        
        // Random opacity and color variations
        particle.style.opacity = Math.random() * 0.5 + 0.3;
        
        particleContainer.appendChild(particle);
    }
}

// ============================================
// INTERACTIVE HOVER EFFECTS - ENTFERNT
// ============================================

function addInteractiveEffects() {
    // ALLE KARTEN-HOVER-EFFEKTE ENTFERNT
    // Kein 3D-Tilt, kein Zoom, keine Bewegung mehr!
    
    // Nur Ripple-Effekte für Contact Items beibehalten
    const contactItems = document.querySelectorAll('.contact-item');
    contactItems.forEach(item => {
        item.addEventListener('click', function(e) {
            const ripple = document.createElement('div');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.cssText = `
                position: absolute;
                width: ${size}px;
                height: ${size}px;
                left: ${x}px;
                top: ${y}px;
                background: rgba(255, 255, 255, 0.3);
                border-radius: 50%;
                transform: scale(0);
                animation: ripple 0.6s ease-out;
                pointer-events: none;
                z-index: 1;
            `;
            
            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
}

// Add ripple animation CSS
const rippleStyle = document.createElement('style');
rippleStyle.textContent = `
    @keyframes ripple {
        to {
            transform: scale(2);
            opacity: 0;
        }
    }
`;
document.head.appendChild(rippleStyle);

// ============================================
// RESPONSIVE UTILITIES
// ============================================

function handleResize() {
    createAdvancedParticles();
    
    // Adjust card size on very small screens
    const card = document.querySelector('.business-card');
    if (window.innerWidth < 400) {
        card.style.fontSize = '0.9rem';
    } else {
        card.style.fontSize = '';
    }
}

// ============================================
// INITIALIZATION - ERWEITERT
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    // Load saved theme
    loadSavedTheme();
    
    // Initialize theme toggle with JavaScript effects
    initThemeToggle();
    
    // Start typing animation
    setTimeout(() => {
        typeWriter();
    }, 1000);
    
    // Initialize animations
    setTimeout(() => {
        initCardAnimation();
        animateCounters();
    }, 500);
    
    // Create particles
    createAdvancedParticles();
    
    // Add interactive effects (ohne Karten-Hover)
    addInteractiveEffects();
    
    // Handle window resize
    window.addEventListener('resize', handleResize);
    
    // Add accessibility features
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Tab') {
            document.body.classList.add('using-keyboard');
        }
    });
    
    document.addEventListener('mousedown', function() {
        document.body.classList.remove('using-keyboard');
    });
});

// ============================================
// PERFORMANCE OPTIMIZATIONS
// ============================================

// Throttle resize events
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Apply throttling to resize handler
window.addEventListener('resize', throttle(handleResize, 100));

// Preload theme transitions
const themePreloader = document.createElement('div');
themePreloader.style.cssText = `
    position: fixed;
    top: -100px;
    left: -100px;
    width: 1px;
    height: 1px;
    opacity: 0;
    pointer-events: none;
`;
document.body.appendChild(themePreloader);

// ============================================
// EASTER EGGS & SPECIAL EFFECTS
// ============================================

let clickCount = 0;

// Warten bis DOM geladen ist für Profile Image Event
document.addEventListener('DOMContentLoaded', function() {
    const profileImage = document.querySelector('.profile-image');
    
    if (profileImage) {
        profileImage.addEventListener('click', function() {
            clickCount++;
            
            if (clickCount === 5) {
                // Secret animation after 5 clicks
                this.style.animation = 'spin 2s ease-in-out';
                
                // Add temporary sparkle effect
                for (let i = 0; i < 12; i++) {
                    const sparkle = document.createElement('div');
                    sparkle.style.cssText = `
                        position: absolute;
                        width: 4px;
                        height: 4px;
                        background: var(--accent-color);
                        border-radius: 50%;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        animation: sparkleExplode 1s ease-out forwards;
                        animation-delay: ${i * 0.1}s;
                    `;
                    this.appendChild(sparkle);
                    
                    setTimeout(() => sparkle.remove(), 1000);
                }
                
                clickCount = 0;
                
                setTimeout(() => {
                    this.style.animation = '';
                }, 2000);
            }
        });
    }
});

// Add sparkle explosion animation
const sparkleStyle = document.createElement('style');
sparkleStyle.textContent = `
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(720deg); }
    }
    
    @keyframes sparkleExplode {
        0% {
            transform: translate(-50%, -50%) scale(0);
            opacity: 1;
        }
        100% {
            transform: translate(-50%, -50%) translate(${Math.random() * 100 - 50}px, ${Math.random() * 100 - 50}px) scale(1);
            opacity: 0;
        }
    }
    
    .using-keyboard *:focus {
        outline: 2px solid var(--accent-color) !important;
        outline-offset: 2px !important;
    }
`;
document.head.appendChild(sparkleStyle);

console.log('🎉 Premium Business Card loaded! Click the profile image 5 times for a surprise!');
