window.onload = function () {
    const loadingScreen = document.getElementById('loadingScreen');
    const scene = document.querySelector('a-scene');
    const marker = document.querySelector('a-marker');
    let markerVisible = false;

    // Hide loading screen once scene is loaded
    scene.addEventListener('loaded', function () {
        loadingScreen.style.display = 'none';
    });

    // Marker found event
    marker.addEventListener('markerFound', function () {
        markerVisible = true;
        console.log('Marker Found');
        // Add any animations or effects when marker is found
    });

    // Marker lost event
    marker.addEventListener('markerLost', function () {
        markerVisible = false;
        console.log('Marker Lost');
        // Add any animations or effects when marker is lost
    });

    // Error handling for video stream
    scene.addEventListener('camera-error', function (event) {
        console.error('Camera error:', event);
        alert('Camera error. Please ensure you have given camera permissions.');
    });

    // Success handling for video stream
    scene.addEventListener('camera-init', function (event) {
        console.log('Camera initialized');
    });
};

// Prevent zoom on double tap
document.addEventListener('dblclick', function (event) {
    event.preventDefault();
}, { passive: false });

AFRAME.registerComponent('clickable', {
    init: function () {
        const el = this.el;
        const textElement = document.querySelector('#description-text');
        let isTextVisible = false;

        // Add touch events for mobile
        el.addEventListener('touchstart', onClick);
        el.addEventListener('click', onClick);

        function onClick(evt) {
            console.log('Image clicked/touched!'); // Debug log
            evt.preventDefault();
            evt.stopPropagation();

            const description = el.getAttribute('data-text');
            console.log('Description:', description); // Debug log

            isTextVisible = !isTextVisible;
            console.log('Text visibility:', isTextVisible); // Debug log

            textElement.setAttribute('value', isTextVisible ? description : '');
            textElement.setAttribute('visible', isTextVisible);
        }

        // Make sure cursor can interact with the image
        el.setAttribute('class', 'clickable');
        el.setAttribute('raycaster-target', '');
    }
});

// Make sure this runs after the scene is loaded
window.addEventListener('load', () => {
    console.log('Page loaded'); // Debug log

    // Add cursor for interaction
    const scene = document.querySelector('a-scene');
    scene.addEventListener('loaded', function () {
        console.log('Scene loaded'); // Debug log

        const camera = document.querySelector('[camera]');
        if (!document.querySelector('[cursor]')) {
            console.log('Adding cursor'); // Debug log
            const cursor = document.createElement('a-entity');
            cursor.setAttribute('cursor', 'rayOrigin: mouse;'); // Changed to mouse-based cursor
            cursor.setAttribute('raycaster', 'objects: .clickable');
            camera.appendChild(cursor);
        }
    });
});
