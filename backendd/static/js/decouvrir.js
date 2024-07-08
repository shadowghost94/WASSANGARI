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
