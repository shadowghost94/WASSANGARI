document.addEventListener('DOMContentLoaded', function() {
    const containerCDs = document.querySelectorAll('.containerCD');
    
    containerCDs.forEach(container => {
        const chantsBtn = container.querySelector('.tabCD-btn#chants-btn');
        const dancesBtn = container.querySelector('.tabCD-btn#dances-btn');
        const chants = container.querySelector('.content#chants');
        const dances = container.querySelector('.content#dances');

        function showSection(sectionToShow, sectionToHide) {
            sectionToShow.classList.add('active');
            sectionToHide.classList.remove('active');
        }

        chantsBtn.addEventListener('click', function() {
            showSection(chants, dances);
        });

        dancesBtn.addEventListener('click', function() {
            showSection(dances, chants);
        });

        // Affiche la section "Chants" par défaut
        showSection(chants, dances);
    });

});
