const track = document.querySelector('.carousel__track');
const slides = Array.from(track.children);
const Nav = document.querySelector('.carousel_nav');
const NavElement = Array.from(Nav.children);


const MoveToSlide = (track, targetSlide) => {
    track.style.transform = 'translateX(-' + targetSlide.style.left + ')';
}

const slideWidth = slides[0].getBoundingClientRect().width;

slides.forEach((slide, i) => {
    slide.style.left = slideWidth * i + 'px';
});

Nav.addEventListener('click', e => {
    const targetElement = e.target.closest('span');

    if (!targetElement) return;

    const currentDot = Nav.querySelector('.current-slide');
    const targetIndex = NavElement.findIndex(dot => dot === targetElement);
    const targetSlide = slides[targetIndex];
    
    MoveToSlide(track, targetSlide);

    currentDot.classList.remove('current-slide');
    targetElement.classList.add('current-slide');
});

var i = 0;

function loop() {
    setTimeout(function() {
        i++;
        NavElement[i].click();
        if (i == (NavElement.length - 1)) {
            i = -1;
        }
        loop();
    }, 5000);
}

loop();