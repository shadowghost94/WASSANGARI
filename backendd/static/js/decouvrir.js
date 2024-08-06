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
            const menuItemss = document.querySelectorAll('.uniqq');
            const contentss = document.querySelectorAll('.content-uniqq');

            menuItemss.forEach(item => {
                item.addEventListener('click', function() {
                    // Remove active class from all menu items and contents
                    menuItemss.forEach(i => i.classList.remove('active'));
                    contentss.forEach(c => c.classList.remove('active'));

                    // Add active class to the clicked menu item and corresponding content
                    item.classList.add('active');
                    document.getElementById(item.getAttribute('data-content')).classList.add('active');
                });
            });
        });

        //3
        document.addEventListener('DOMContentLoaded', function() {
            const menuItemss = document.querySelectorAll('.uniqqq');
            const contentss = document.querySelectorAll('.content-uniqqq');

            menuItemss.forEach(item => {
                item.addEventListener('click', function() {
                    // Remove active class from all menu items and contents
                    menuItemss.forEach(i => i.classList.remove('active'));
                    contentss.forEach(c => c.classList.remove('active'));

                    // Add active class to the clicked menu item and corresponding content
                    item.classList.add('active');
                    document.getElementById(item.getAttribute('data-content')).classList.add('active');
                });
            });
        });

        //4
        document.addEventListener('DOMContentLoaded', function() {
            const menuItemss = document.querySelectorAll('.uniqqqq');
            const contentss = document.querySelectorAll('.content-uniqqqq');

            menuItemss.forEach(item => {
                item.addEventListener('click', function() {
                    // Remove active class from all menu items and contents
                    menuItemss.forEach(i => i.classList.remove('active'));
                    contentss.forEach(c => c.classList.remove('active'));

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
        function togggleText() {
            const content = document.getElementById('content-detaill');
            const icon = document.getElementById('toggle-iconn');
            content.classList.toggle('hidden');
            icon.classList.toggle('rotate');
        }
        function toggggleText() {
            const content = document.getElementById('content-detailll');
            const icon = document.getElementById('toggle-iconnn');
            content.classList.toggle('hidden');
            icon.classList.toggle('rotate');
        }
        function togggggleText() {
            const content = document.getElementById('content-detaillll');
            const icon = document.getElementById('toggle-iconnnn');
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

/* Sections découvrir bénin politique */
document.getElementById('item-decouvrir-benin-politique').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.grid-decouvrir-benin').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('back-to-main1').style.display = 'none';
    document.getElementById('decouvrir-benin-politique').style.display = 'block';
});

document.getElementById('back-to-main4').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.grid-decouvrir-benin').forEach(function(item) {
        item.style.display = 'grid';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('back-to-main1').style.display = 'block';
    document.getElementById('decouvrir-benin-politique').style.display = 'none';
});

/* Sections découvrir bénin économie */
document.getElementById('item-decouvrir-benin-economie').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.grid-decouvrir-benin').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('back-to-main1').style.display = 'none';
    document.getElementById('decouvrir-benin-economie').style.display = 'block';
});

document.getElementById('back-to-main5').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.grid-decouvrir-benin').forEach(function(item) {
        item.style.display = 'grid';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('back-to-main1').style.display = 'block';
    document.getElementById('decouvrir-benin-economie').style.display = 'none';
});



/* ETHNIES OPTIONS */
document.getElementById('decouvr-eth').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.item-decouvrir').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('ethnie-div-div').style.display = 'flex';
    document.getElementById('back-to-main6').style.display='block'
});

document.getElementById('back-to-main6').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.item-decouvrir').forEach(function(item) {
        item.style.display = 'flex';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('ethnie-div-div').style.display = 'none';
    document.getElementById('back-to-main6').style.display = 'none';
});

/* LANGUES OPTIONS */
document.getElementById('decouvr-lang').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.item-decouvrir').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('langue-div-div').style.display = 'flex';
    document.getElementById('back-to-main7').style.display='block'
});

document.getElementById('back-to-main7').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.item-decouvrir').forEach(function(item) {
        item.style.display = 'flex';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('langue-div-div').style.display = 'none';
    document.getElementById('back-to-main7').style.display = 'none';
});

/* GASTRONOMIE OPTIONS */
document.getElementById('decouvr-gastr').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.item-decouvrir').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('gastro-div-div').style.display = 'flex';
    document.getElementById('back-to-main8').style.display='block'
});

document.getElementById('back-to-main8').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.item-decouvrir').forEach(function(item) {
        item.style.display = 'flex';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('gastro-div-div').style.display = 'none';
    document.getElementById('back-to-main8').style.display = 'none';
});

/* DIVINITES OPTIONS */
document.getElementById('decouvr-divinites').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.item-decouvrir').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('divinites-div-div').style.display = 'flex';
    document.getElementById('back-to-main9').style.display='block'
});

document.getElementById('back-to-main9').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.item-decouvrir').forEach(function(item) {
        item.style.display = 'flex';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('divinites-div-div').style.display = 'none';
    document.getElementById('back-to-main9').style.display = 'none';
});

/* HISTOIRE OPTIONS */
document.getElementById('decouvr-histoire').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.item-decouvrir').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('histoire-div-div').style.display = 'flex';
    document.getElementById('back-to-main10').style.display='block'
});

document.getElementById('back-to-main10').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.item-decouvrir').forEach(function(item) {
        item.style.display = 'flex';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('histoire-div-div').style.display = 'none';
    document.getElementById('back-to-main10').style.display = 'none';
});


/* DECOUVRIR CHANTS ET DANSES */
document.getElementById('decouvr-cd').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.item-decouvrir').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('chants-danses-div-div').style.display = 'flex';
    document.getElementById('back-to-main13').style.display='block';
});

document.getElementById('back-to-main13').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.item-decouvrir').forEach(function(item) {
        item.style.display = 'flex';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('chants-danses-div-div').style.display = 'none';
    document.getElementById('back-to-main13').style.display = 'none';
});

// chants danses
function showRest(ethnieId) {
    
    const grids = document.querySelectorAll('.grid-item-chants-danses');
    const detail = document.getElementById(ethnieId);

    grids.forEach( contain => {
        contain.style.display = 'none';
    });
    document.getElementById('back-to-main13').style.display = 'none';
    document.getElementById('back-to-main-danses-div').style.display = 'block';
    detail.style.display = 'block';
}
document.getElementById('back-to-main-danses-div').addEventListener('click', function() {
    document.getElementById('back-to-main-danses-div').style.display = 'none';
    const containers = document.getElementsByClassName('containerCD');
    
    // Convertir la collection HTML en un tableau pour pouvoir utiliser forEach
    Array.from(containers).forEach(container => {
        container.style.display = 'none';
    });

    const grids = document.querySelectorAll('.grid-item-chants-danses');
    grids.forEach( contain => {
        contain.style.display = 'flex';
    });
    document.getElementById('back-to-main13').style.display = 'block';
});