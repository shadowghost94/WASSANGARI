function showEventDetails(eventId) {
    const modal = document.getElementById(eventId.toString());
    const eventMen = document.getElementById("header--wrapper");
    eventMen.style.display = "none";
    modal.style.display = "block";
}

function closeEventDetails(eventId) {
    const modal = document.getElementById(eventId.toString());
    const eventMen = document.getElementById("header--wrapper");
    eventMen.style.display = "flex";
    modal.style.display = "none";
}