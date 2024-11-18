document.addEventListener("DOMContentLoaded", function () {
    // Traverse every update item
    document.querySelectorAll('.accordion-item').forEach(function (accordionItem) {
        const stars = accordionItem.querySelectorAll(".rating .star");
        const output = accordionItem.querySelector("#rating-output");
        const submitButton = accordionItem.querySelector("#submit-rating");
        const ratingScoreInput = accordionItem.querySelector("#rating-score"); // rating score input
        let selectedRating = 0; // Stores the rating selected by the user

        // Function to update star colors based on the given rating
        function updateStars(rating) {
            stars.forEach(star => {
                const starValue = parseInt(star.getAttribute("data-value"), 10);
                star.classList.toggle("selected", starValue <= rating);
            });
        }

        // On mouseover, update star colors to show the current hovered rating
        stars.forEach(star => {
            star.addEventListener("mouseover", function () {
                if (selectedRating === 0) { // Only update if no rating is fixed
                    const ratingValue = parseInt(this.getAttribute("data-value"), 10);
                    updateStars(ratingValue);
                }
            });

            // On star click, fix the selected rating
            star.addEventListener("click", function () {
                const ratingValue = parseInt(this.getAttribute("data-value"), 10);
                selectedRating = (selectedRating === ratingValue) ? 0 : ratingValue; // Toggle the rating
                updateStars(selectedRating);
                output.textContent = selectedRating ? `Score: ${selectedRating}` : '';
                //submitButton.disabled = selectedRating === 0; 
                ratingScoreInput.value = selectedRating;
            });
        });

        // On mouse leave, reset stars only if no rating is selected
        accordionItem.querySelector(".rating").addEventListener("mouseleave", function () {
            if (selectedRating === 0) { // Reset only if no rating is fixed
                updateStars(0);
            }
        });

        // Handle submit button click
        submitButton.addEventListener('click', function () {
            if (selectedRating === 0) {
                return; // Don't submit if no rating is selected
            }


        });
    });
});


