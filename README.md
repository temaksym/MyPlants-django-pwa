# My Django PWA

This project is a Progressive Web App (PWA) built using Django, HTML, CSS, and JavaScript. It demonstrates how to create a web application that can work offline and provide a native app-like experience.

## Project Structure

```
my-django-pwa
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates
│   │   └── app
│   │       └── index.html
│   └── static
│       ├── css
│       │   └── styles.css
│       ├── js
│       │   └── main.js
│       └── images
├── pwa
│   ├── __init__.py
│   ├── manifest.json
│   └── serviceworker.js
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd my-django-pwa
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```
   python manage.py migrate
   ```

5. **Run the development server:**
   ```
   python manage.py runserver
   ```

6. **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage Guidelines

- The application is structured to support PWA features, including offline capabilities and caching.
- The `manifest.json` file contains metadata for the PWA, such as the app name, icons, and theme color.
- The `serviceworker.js` file handles caching and offline functionality.

## Contributing

Feel free to submit issues or pull requests to improve the project. Contributions are welcome!