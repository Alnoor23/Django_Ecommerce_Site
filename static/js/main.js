const hamburger = document.querySelector('#hamburger');
const hamburger1 = document.querySelector('.header__wrap__toggle');
const menu = document.querySelector('.header__menu');
const header = document.querySelector('.header');
const overlay = document.querySelector('.overlay');
const fadeElems = document.querySelectorAll('.has-fade');
const body = document.querySelector('body');


hamburger.addEventListener('click', function(){
    if(header.classList.contains('open')){ // close
        header.classList.remove('open');
        body.classList.remove('noscroll');
        hamburger1.classList.remove('to-white');
        fadeElems.forEach(function(element){
            element.classList.remove('fade-in');
            element.classList.add('fade-out');    
        });
    }
    else { // open
        body.classList.add('noscroll');
        header.classList.add('open');
        hamburger1.classList.add('to-white');
        fadeElems.forEach(function(element){
            element.classList.remove('fade-out');
            element.classList.add('fade-in');
        });
    }
});
