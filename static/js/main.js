document.addEventListener('DOMContentLoaded', function() {
    var menuToggle = document.getElementById('mobile-menu');
    var closeBtn = document.getElementById('close-btn');
    var navbar = document.querySelector('.navbar');
    var navList = document.getElementById('nav-list');
    menuToggle.addEventListener('click', function() {
        navbar.classList.add('active');
    });
    closeBtn.addEventListener('click', function() {
        navbar.classList.remove('active');
    });
    // Cerrar el menú al hacer clic en un enlace (si es necesario)
    navList.addEventListener('click', function(e) {
        if (e.target.tagName === 'A') {
            navbar.classList.remove('active');
        }
    });
    // Cerrar el menú al hacer clic fuera de él
    document.getElementById('content').addEventListener('click', function() {
        navbar.classList.remove('active');
    });
});
// dhdh
document.addEventListener('DOMContentLoaded', function() {
    var menuToggle = document.getElementById('mobile-menu');
    var closeBtn = document.getElementById('close-btn');
    var navbar = document.querySelector('.navbar');
    var navList = document.getElementById('nav-list');
    menuToggle.addEventListener('click', function() {
        navList.classList.toggle('active');
    });
    closeBtn.addEventListener('click', function() {
        navList.classList.remove('active');
    });
    // Cerrar el menú al hacer clic en un enlace
    navList.addEventListener('click', function(e) {
        if (e.target.tagName === 'A' && window.innerWidth < 769) {
            navList.classList.remove('active');
        }
    });
    // Cerrar el menú al hacer clic fuera de él
    document.getElementById('content').addEventListener('click', function() {
        if (window.innerWidth < 769) {
            navList.classList.remove('active');
        }
    });
});