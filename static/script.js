// ===============================
// Slider
// ===============================

const slides = document.querySelectorAll(".slide");
const dots = document.querySelectorAll(".dot");

const nextBtn = document.querySelector(".next");
const prevBtn = document.querySelector(".prev");

let current = 0;
let interval;

// ===============================

function showSlide(index) {

    slides.forEach(slide => {
        slide.classList.remove("active");
    });

    dots.forEach(dot => {
        dot.classList.remove("active");
    });

    slides[index].classList.add("active");
    dots[index].classList.add("active");

}

// ===============================

function nextSlide() {

    current++;

    if (current >= slides.length) {

        current = 0;

    }

    showSlide(current);

}

// ===============================

function prevSlide() {

    current--;

    if (current < 0) {

        current = slides.length - 1;

    }

    showSlide(current);

}

// ===============================

nextBtn.addEventListener("click", () => {

    nextSlide();

    restartSlider();

});

prevBtn.addEventListener("click", () => {

    prevSlide();

    restartSlider();

});

// ===============================

dots.forEach((dot, index) => {

    dot.addEventListener("click", () => {

        current = index;

        showSlide(current);

        restartSlider();

    });

});

// ===============================

function autoSlider() {

    interval = setInterval(() => {

        nextSlide();

    }, 5000);

}

function restartSlider() {

    clearInterval(interval);

    autoSlider();

}

autoSlider();

// ===============================
// Pause on Hover
// ===============================

const slider = document.querySelector(".slider");

slider.addEventListener("mouseenter", () => {

    clearInterval(interval);

});

slider.addEventListener("mouseleave", () => {

    autoSlider();

});

// ===============================
// Scroll Animation
// ===============================

const observer = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            entry.target.classList.add("show");

        }

    });

}, {
    threshold: 0.2
});

document.querySelectorAll(
    ".service-card,.advantage,.contact,.section-title"
).forEach(item => {

    item.classList.add("hidden");

    observer.observe(item);

});

// ===============================
// Smooth Scroll
// ===============================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        e.preventDefault();

        const target = document.querySelector(
            this.getAttribute("href")
        );

        if (target) {

            target.scrollIntoView({

                behavior: "smooth"

            });

        }

    });

});

// ===============================
// Header Shadow
// ===============================

const header = document.querySelector("header");

window.addEventListener("scroll", () => {

    if (window.scrollY > 30) {

        header.style.boxShadow = "0 15px 35px rgba(0,0,0,.15)";

    } else {

        header.style.boxShadow = "0 3px 20px rgba(0,0,0,.08)";

    }

});

// ===============================
// Animation Classes
// ===============================

const style = document.createElement("style");

style.innerHTML = `

.hidden{

opacity:0;

transform:translateY(60px);

transition:.8s;

}

.show{

opacity:1;

transform:translateY(0);

}

`;

document.head.appendChild(style);

// ===============================
// Current Year
// ===============================

const copy = document.querySelector(".copyright");

if (copy) {

    copy.innerHTML = `© ${new Date().getFullYear()} Все права защищены.`;

}


document.addEventListener("DOMContentLoaded", () => {

    const phoneInput = document.getElementById("phone");
    const error = document.getElementById("phone-error");

    const regex = /^\+994(50|51|55|70|77|99|10)\d{7}$/;

    phoneInput.addEventListener("input", function () {

        const value = this.value.trim();

        if (value === "") {
            this.classList.remove("valid", "invalid");
            error.textContent = "";
            return;
        }

        if (regex.test(value)) {
            this.classList.remove("invalid");
            this.classList.add("valid");
            error.textContent = "";
        } else {
            this.classList.remove("valid");
            this.classList.add("invalid");
            error.textContent = "Telefon nömrəsi düzgün deyil.";
        }
    });

});