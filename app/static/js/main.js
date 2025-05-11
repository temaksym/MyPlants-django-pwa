// Function to toggle navigation menu visibility
function toggleNavMenu() {
    const navMenu = document.getElementById('nav-menu');
    navMenu.style.left = navMenu.style.left === '0px' ? '-250px' : '0px';
}

// Add event listener to the menu icon
document.addEventListener('DOMContentLoaded', () => {
    const menuIcon = document.getElementById('menu');
    const navMenu = document.getElementById('nav-menu');
    const closeIcon = document.getElementById('menu-arrow');

    menuIcon.addEventListener('click', toggleNavMenu);
    closeIcon.addEventListener('click', toggleNavMenu)
});
