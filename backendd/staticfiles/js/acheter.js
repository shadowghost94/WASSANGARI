function showAchatDetails(eventId) {
    const modal = document.getElementById(eventId.toString());
    const eventMen = document.getElementById("header--wrapper");
    eventMen.style.display = "none";
    modal.style.display = "block";
}

function closeAchatDetails(eventId) {
    const modal = document.getElementById(eventId.toString());
    const eventMen = document.getElementById("header--wrapper");
    eventMen.style.display = "flex";
    modal.style.display = "none";
}