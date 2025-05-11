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






// Function to create popup for adding new plant
function createPopup() {
    const popup = document.createElement('div');
    popup.className = 'popup';
    popup.innerHTML = `
        <div class="popup-content">
            <span class="close" id="close-popup">&times;</span>
            <h2>Add New Plant</h2>
            <form id="add-plant-form">
                <label for="plant-name">Plant Name:</label>
                <input type="text" id="plant-name" name="plant-name" required>
                <label for="plant-type">Plant Type:</label>
                <input type="text" id="plant-type" name="plant-type" required>
                <button type="submit">Add Plant</button>
            </form>
        </div>`;
    document.body.appendChild(popup);

    // Close the popup when the close button is clicked
    const closeButton = document.getElementById('close-popup');
    closeButton.addEventListener('click', () => {
        document.body.removeChild(popup);
    });

    // Handle form submission
    const form = document.getElementById('add-plant-form');
    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const plantName = document.getElementById('plant-name').value;
        const plantType = document.getElementById('plant-type').value;

        try {
            const response = await fetch('/api/plants/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ name: plantName, type: plantType })
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            alert('Plant added successfully!');
            document.body.removeChild(popup);
        } catch (error) {
            console.error('Error adding plant:', error);
        }
    });
}