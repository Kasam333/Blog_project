// Function to filter posts based on the selected category
function filterCategory(category) {
    // Remove active class from all buttons
    const buttons = document.querySelectorAll('.category-btn');
    buttons.forEach(button => button.classList.remove('active'));

    // Add active class to the selected button
    const selectedButton = document.querySelector(`.category-btn[onclick*="${category}"]`);
    if (selectedButton) {
        selectedButton.classList.add('active');
    }


    const posts = document.querySelectorAll('.post');

    if (category === 'All') {
        // Show all posts when "All Categories" is clicked
        posts.forEach(post => {
            post.style.display = 'block';
        });
    } else {
        // Loop through all posts and show those that match the selected category
        posts.forEach(post => {
            if (post.getAttribute('data-category') === category) {
                post.style.display = 'block';
            } else {
                post.style.display = 'none';
            }
        });
    }
}

// Display all posts by default when the page loads
document.addEventListener('DOMContentLoaded', function () {
    filterCategory('All');
});


