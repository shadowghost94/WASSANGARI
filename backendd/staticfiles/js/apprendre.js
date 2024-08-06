document.getElementById('apprend-benin').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.item-apprendre').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('apprendre-benin').style.display = 'block';
});

document.getElementById('appr-back-to-main1').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.item-apprendre').forEach(function(item) {
        item.style.display = 'flex';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('apprendre-benin').style.display = 'none';
});


// SEction apprendre histoire
document.getElementById('item-apprendre-benin-histoire').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.grid-apprendre-benin').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('appr-back-to-main1').style.display = 'none';
    document.getElementById('apprendre-benin-histoire').style.display = 'block';
});

document.getElementById('appr-back-to-main2').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.grid-apprendre-benin').forEach(function(item) {
        item.style.display = 'grid';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('appr-back-to-main1').style.display = 'block';
    document.getElementById('apprendre-benin-histoire').style.display = 'none';
});

        /* Javascript pour gérer le defilement podcast-text-apprendre-videos-images */
        document.addEventListener('DOMContentLoaded', function() {
            const menuItems = document.querySelectorAll('.uniq');
            const contents = document.querySelectorAll('.appr-content-uniq');

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
            const contentss = document.querySelectorAll('.appr-content-uniqq');

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
            const contentss = document.querySelectorAll('.appr-content-uniqqq');

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
            const contentss = document.querySelectorAll('.appr-content-uniqqqq');

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
            const content = document.getElementById('appr-content-detail');
            const icon = document.getElementById('toggle-icon');
            content.classList.toggle('hidden');
            icon.classList.toggle('rotate');
        }
        function togggleText() {
            const content = document.getElementById('appr-content-detaill');
            const icon = document.getElementById('toggle-iconn');
            content.classList.toggle('hidden');
            icon.classList.toggle('rotate');
        }
        function toggggleText() {
            const content = document.getElementById('appr-content-detailll');
            const icon = document.getElementById('toggle-iconnn');
            content.classList.toggle('hidden');
            icon.classList.toggle('rotate');
        }
        function togggggleText() {
            const content = document.getElementById('appr-content-detaillll');
            const icon = document.getElementById('toggle-iconnnn');
            content.classList.toggle('hidden');
            icon.classList.toggle('rotate');
        }
        document.querySelectorAll('.question-summary').forEach(item => {
            item.addEventListener('click', () => {
                const detail = item.nextElementSibling;
                const icon = item.querySelector('.fas');
        
                if (detail.style.display === 'block') {
                    detail.style.display = 'none';
                    icon.classList.remove('fa-chevron-up');
                    icon.classList.add('fa-chevron-down');
                } else {
                    detail.style.display = 'block';
                    icon.classList.remove('fa-chevron-down');
                    icon.classList.add('fa-chevron-up');
                }
            });
        });
        
/* Sections découvrir bénin géographie */
document.getElementById('item-apprendre-benin-geographie').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.grid-apprendre-benin').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('appr-back-to-main1').style.display = 'none';
    document.getElementById('apprendre-benin-geographie').style.display = 'block';
});

document.getElementById('appr-back-to-main3').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.grid-apprendre-benin').forEach(function(item) {
        item.style.display = 'grid';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('appr-back-to-main1').style.display = 'block';
    document.getElementById('apprendre-benin-geographie').style.display = 'none';
});

/* Sections découvrir bénin politique */
document.getElementById('item-apprendre-benin-politique').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.grid-apprendre-benin').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('appr-back-to-main1').style.display = 'none';
    document.getElementById('apprendre-benin-politique').style.display = 'block';
});

document.getElementById('appr-back-to-main4').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.grid-apprendre-benin').forEach(function(item) {
        item.style.display = 'grid';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('appr-back-to-main1').style.display = 'block';
    document.getElementById('apprendre-benin-politique').style.display = 'none';
});

/* Sections découvrir bénin économie */
document.getElementById('item-apprendre-benin-economie').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.grid-apprendre-benin').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('appr-back-to-main1').style.display = 'none';
    document.getElementById('apprendre-benin-economie').style.display = 'block';
});

document.getElementById('appr-back-to-main5').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.grid-apprendre-benin').forEach(function(item) {
        item.style.display = 'grid';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('appr-back-to-main1').style.display = 'block';
    document.getElementById('apprendre-benin-economie').style.display = 'none';
});



/* ETHNIES OPTIONS */
document.getElementById('apprend-eth').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.item-apprendre').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('appr-ethnie-div-div').style.display = 'flex';
    document.getElementById('appr-back-to-main6').style.display='block'
});

document.getElementById('appr-back-to-main6').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.item-apprendre').forEach(function(item) {
        item.style.display = 'flex';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('appr-ethnie-div-div').style.display = 'none';
    document.getElementById('appr-back-to-main6').style.display = 'none';
});

/* LANGUES OPTIONS */
document.getElementById('apprend-lang').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.item-apprendre').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('appr-langue-div-div').style.display = 'flex';
    document.getElementById('appr-back-to-main7').style.display='block'
});

document.getElementById('appr-back-to-main7').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.item-apprendre').forEach(function(item) {
        item.style.display = 'flex';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('appr-langue-div-div').style.display = 'none';
    document.getElementById('appr-back-to-main7').style.display = 'none';
});

/* GASTRONOMIE OPTIONS */
document.getElementById('apprend-gastr').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.item-apprendre').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('appr-gastro-div-div').style.display = 'flex';
    document.getElementById('appr-back-to-main8').style.display='block'
});

document.getElementById('appr-back-to-main8').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.item-apprendre').forEach(function(item) {
        item.style.display = 'flex';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('appr-gastro-div-div').style.display = 'none';
    document.getElementById('appr-back-to-main8').style.display = 'none';
});

/* DIVINITES OPTIONS */
document.getElementById('apprend-divinites').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.item-apprendre').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('appr-divinites-div-div').style.display = 'flex';
    document.getElementById('appr-back-to-main9').style.display='block';
});

document.getElementById('appr-back-to-main9').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.item-apprendre').forEach(function(item) {
        item.style.display = 'flex';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('appr-divinites-div-div').style.display = 'none';
    document.getElementById('appr-back-to-main9').style.display = 'none';
});

/* HISTOIRE OPTIONS */
document.getElementById('apprend-histoire').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.item-apprendre').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('appr-histoire-div-div').style.display = 'flex';
    document.getElementById('appr-back-to-main10').style.display='block'
});

document.getElementById('appr-back-to-main10').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.item-apprendre').forEach(function(item) {
        item.style.display = 'flex';
        item.style.alignItems = 'center';      // Alignement vertical au centre
        item.style.justifyContent = 'center';  // Alignement horizontal au centre
    });
    document.getElementById('appr-histoire-div-div').style.display = 'none';
    document.getElementById('appr-back-to-main10').style.display = 'none';
});