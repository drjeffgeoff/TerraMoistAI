
document.addEventListener("DOMContentLoaded", function() {
    function formatDate(date) {
        const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        return date.toLocaleDateString(undefined, options);
    }

    const currentDateElement = document.getElementById('current-date');
    const currentDate = new Date();
    currentDateElement.textContent = formatDate(currentDate);

});