self.addEventListener('install', function(event) {
    event.waitUntil(
        caches.open('my-django-pwa-cache').then(function(cache) {
            return cache.addAll([
                '/',
                '/index.html',
                '/static/css/styles.css',
                '/static/js/main.js',
                '/static/images/favicon.png', // Add your image paths here
            ]);
        })
    );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request).then(function(response) {
            return response || fetch(event.request);
        })
    );
});

self.addEventListener('activate', function(event) {
    var cacheWhitelist = ['my-django-pwa-cache'];
    event.waitUntil(
        caches.keys().then(function(cacheNames) {
            return Promise.all(
                cacheNames.map(function(cacheName) {
                    if (cacheWhitelist.indexOf(cacheName) === -1) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});