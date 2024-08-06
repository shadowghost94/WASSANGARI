function showActuDetails(eventId) {
    const modal = document.getElementById("informer" + eventId.toString());
    const articles = document.querySelectorAll(".article");

    articles.forEach(article => {
        article.style.display = "none";
    });
    if (modal) {
        modal.style.display = "flex";
    } else {
        console.error('Modal not found: ' + 'informer' + eventId);
    }
}

function closeActuDetails(eventId) {
    const modal = document.getElementById("informer" + eventId.toString());
    const articles = document.querySelectorAll(".article");

    articles.forEach(article => {
        article.style.display = "flex";
    });
    if (modal) {
        modal.style.display = "none";
    } else {
        console.error('Modal not found: ' + 'informer' + eventId);
    }
}

document.addEventListener('DOMContentLoaded', (event) => {
    const articles = document.querySelectorAll('.article');
    articles.forEach(article => {
        article.addEventListener('click', function() {
            const eventId = this.getAttribute('onclick').match(/\d+/)[0];
            showActuDetails(eventId);
        });
    });
});
