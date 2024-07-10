document.getElementById('decouvr-benin').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.item-decouvrir').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('decouvrir-benin').style.display = 'block';
});

document.getElementById('back-to-main1').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.item-decouvrir').forEach(function(item) {
        item.style.display = 'flex';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('decouvrir-benin').style.display = 'none';
});


// SEction decouvrir histoire
document.getElementById('item-decouvrir-benin-histoire').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.grid-decouvrir-benin').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('back-to-main1').style.display = 'none';
    document.getElementById('decouvrir-benin-histoire').style.display = 'block';
});

document.getElementById('back-to-main2').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.grid-decouvrir-benin').forEach(function(item) {
        item.style.display = 'grid';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('back-to-main1').style.display = 'block';
    document.getElementById('decouvrir-benin-histoire').style.display = 'none';
});

        /* Javascript pour gérer le defilement podcast-text-decouvrir-videos-images */
        document.addEventListener('DOMContentLoaded', function() {
            const menuItems = document.querySelectorAll('.uniq');
            const contents = document.querySelectorAll('.content-uniq');

            menuItems.forEach(item => {
                item.addEventListener('click', function() {
                    // Remove active class from all menu items and contents
                    menuItems.forEach(i => i.classList.remove('active'));
                    contents.forEach(c => c.classList.remove('active'));

                    // Add active class to the clicked menu item and corresponding content
                    item.classList.add('active');
                    document.getElementById(item.getAttribute('data-content')).classList.add('active');
                });
            });
        });

        // 2
        document.addEventListener('DOMContentLoaded', function() {
            const menuItems = document.querySelectorAll('.uniqq');
            const contents = document.querySelectorAll('.content-uniqq');

            menuItems.forEach(item => {
                item.addEventListener('click', function() {
                    // Remove active class from all menu items and contents
                    menuItems.forEach(i => i.classList.remove('active'));
                    contents.forEach(c => c.classList.remove('active'));

                    // Add active class to the clicked menu item and corresponding content
                    item.classList.add('active');
                    document.getElementById(item.getAttribute('data-content')).classList.add('active');
                });
            });
        });

        /* le texte quand on clique les détils se ferme puis s'ouvre au click */
        function toggleText() {
            const content = document.getElementById('content-detail');
            const icon = document.getElementById('toggle-icon');
            content.classList.toggle('hidden');
            icon.classList.toggle('rotate');
        }

/* Sections découvrir bénin géographie */
document.getElementById('item-decouvrir-benin-geographie').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.grid-decouvrir-benin').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('back-to-main1').style.display = 'none';
    document.getElementById('decouvrir-benin-geographie').style.display = 'block';
});

document.getElementById('back-to-main3').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.grid-decouvrir-benin').forEach(function(item) {
        item.style.display = 'grid';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('back-to-main1').style.display = 'block';
    document.getElementById('decouvrir-benin-geographie').style.display = 'none';
});