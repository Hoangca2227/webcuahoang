document.addEventListener('DOMContentLoaded', function() {
    // Function to animate the service icons
    function animateServiceIcons() {
        const serviceIcons = document.querySelectorAll('.service-icon');

        serviceIcons.forEach((icon, index) => {
            // Add a slight delay to each icon's animation
            const delay = index * 100;
            setTimeout(() => {
                icon.style.opacity = '0';
                icon.style.transform = 'scale(0.5)';

                // Trigger reflow
                void icon.offsetWidth;

                // Apply animations
                icon.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                icon.style.opacity = '1';
                icon.style.transform = 'scale(1)';
            }, delay);
        });
    }

    // Animate icons on page load
    animateServiceIcons();

    // Optional: Add click event for service icons to navigate to their pages
    const serviceIcons = document.querySelectorAll('.service-icon');
    serviceIcons.forEach(icon => {
        icon.addEventListener('click', function() {
            const serviceId = this.getAttribute('data-service-id');
            // You could navigate to a detail page, or scroll to a specific section
            // For now, let's just log the service ID
            console.log(`Service clicked: ${serviceId}`);

            // Example: Scroll to the relevant section if it exists
            const serviceSection = document.getElementById(`service-detail-${serviceId}`);
            if (serviceSection) {
                serviceSection.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});
