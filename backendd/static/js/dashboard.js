document.getElementById('dash-modif-profil1').addEventListener('click', function() {
    // Masquer toutes les sections grid-item
    document.querySelectorAll('.div-dashboard-principale').forEach(function(item) {
        item.style.display = 'none';
    });
    document.getElementById('modif-afficher').style.display = 'block';
});

document.getElementById('back-to-main1').addEventListener('click', function() {
    // Afficher toutes les sections grid-item
    document.querySelectorAll('.div-dashboard-principale').forEach(function(item) {
        item.style.display = 'flex';
    });
    document.getElementById('modif-afficher').style.display = 'none';
});

//permet de visualiser une photo sélectionné
function previewProfilePic(event) {
    const reader = new FileReader();
    reader.onload = function() {
        const output = document.getElementById('profile-pic-das');
        output.src = reader.result;
    };
    reader.readAsDataURL(event.target.files[0]);
}

//enregistrement des nouvelles informations
document.getElementById('profile-form-das').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    console.log(formData);
    $.ajax({
        url: '{% url "modifierProfil" %}',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        },
        success: function(response) {
            if (response.success) {
                document.getElementById('responseMessage').innerText = 'Votre profil a été modifié avec succès';
            } else {
                document.getElementById('responseMessage').innerText = 'Une erreur medium est survenue lors de la mise à jour du profil';
            }
        },
        error: function() {
            document.getElementById('responseMessage').innerText = 'Une erreur est survenue lors de la mise à jour du profil';
        }
    });
});
