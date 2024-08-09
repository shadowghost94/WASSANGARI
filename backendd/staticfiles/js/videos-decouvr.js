document.addEventListener('DOMContentLoaded', function() {
    const thumbnails = document.querySelectorAll('.video-thumbnail-pol');
    const autoplayDuration = 5000; // Durée en millisecondes (5 secondes)

    thumbnails.forEach(thumbnail => {
        const video = thumbnail.querySelector('.video-preview-pol');

        // Lancer la vidéo automatiquement après le chargement de la page
        video.addEventListener('loadedmetadata', function() {
            video.play();
            
            // Arrêter la vidéo après autoplayDuration
            setTimeout(function() {
                video.pause();
            }, autoplayDuration);
        });

        // Écouteur pour ouvrir la vidéo dans le modal
        thumbnail.addEventListener('click', function() {
            const videoUrl = video.src;
            const videoTitle = thumbnail.querySelector('.video-title-pol').textContent;

            const modal = document.getElementById('videoModal-pol');
            const videoPlayer = document.getElementById('videoPlayer-pol');
            const modalVideoTitle = document.querySelector('.modal-video-title-pol');

            videoPlayer.src = videoUrl;
            modalVideoTitle.textContent = videoTitle;
            modal.style.display = 'block';
        });
    });

    const closeBtn = document.querySelector('.close-pol');
    closeBtn.addEventListener('click', function() {
        const videoPlayer = document.getElementById('videoPlayer-pol');
        videoPlayer.pause();
        videoPlayer.src = ''; // Réinitialiser la source vidéo
        const modal = document.getElementById('videoModal-pol');
        modal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        const modal = document.getElementById('videoModal-pol');
        if (event.target === modal) {
            const videoPlayer = document.getElementById('videoPlayer-pol');
            videoPlayer.pause();
            videoPlayer.src = ''; // Réinitialiser la source vidéo
            modal.style.display = 'none';
        }
    });
});
