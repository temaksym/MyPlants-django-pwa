// This file contains the JavaScript code for the application, including any PWA-related functionality.

// if ('serviceWorker' in navigator) {
//     window.addEventListener('load', () => {
//         navigator.serviceWorker.register('/pwa/serviceworker.js')
//             .then(registration => {
//                 console.log('ServiceWorker registration successful with scope: ', registration.scope);
//             })
//             .catch(error => {
//                 console.log('ServiceWorker registration failed: ', error);
//             });
//     });
// }

// function updateOnlineStatus() {
//     const status = document.getElementById('status');
//     status.innerHTML = navigator.onLine ? 'Online' : 'Offline';
// }

// window.addEventListener('online', updateOnlineStatus);
// window.addEventListener('offline', updateOnlineStatus);

// document.addEventListener('DOMContentLoaded', () => {
//     updateOnlineStatus();
// });



// This function fetches articles from the Django backend and displays them on the page.
async function fetchArticles() {

    let url;
    if (document.title === "Flowers - Articles") {
        url = '/api/articles/';
    } else if (document.title === "Flowers") {
        url = '/api/popular_articles/';
    } else {
        url = ''
    }

    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const articles = await response.json();
        const articlesContainer = document.getElementById('articles-container');

        articles.forEach(article => {
            console.log(article);
            const articleLink = document.createElement('a');
            articleLink.href = `/article/${article.id}/`;
            articleLink.className = 'article-link';

            const articleBlock = document.createElement('div');
            articleBlock.className = 'article-block';

            const textBlock = document.createElement('div');
            textBlock.className = 'text-block';

            const articleImage = document.createElement('img');
            articleImage.src = '/static/images/flower-article.png';

            const title = document.createElement('h3');
            title.textContent = article.title;

            const content = document.createElement('p');
            content.textContent = article.content.substring(0, 100) + '...';

            articleBlock.appendChild(articleImage)
            textBlock.appendChild(title);
            textBlock.appendChild(content);
            articleBlock.appendChild(textBlock);
            articleLink.appendChild(articleBlock);

            articlesContainer.appendChild(articleLink);
        });
    } catch (error) {
        console.error('Error fetching articles:', error);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    if (document.title === "Flowers - Articles" || document.title === "Flowers") {
        fetchArticles();
    }
});



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