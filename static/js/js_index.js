
function afficherSection(sectionId) {
    // Cacher toutes les sections
    event.preventDefault();
    var sections = document.getElementsByClassName('section');
    for (var i = 0; i < sections.length; i++) {
        sections[i].style.display = 'none';
    }

    // Afficher la section spécifiée
    var section = document.getElementById(sectionId);
    section.style.display = 'block';

    // Mettre à jour la couleur des boutons
    var buttons = document.getElementsByTagName('button');
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove('active');
    }

    var activeButton = document.getElementById('btn' + sectionId);
    activeButton.classList.add('active');
}
