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

function updateClubPoints() {
    fetch('/getClubData') 
        .then(response => response.json())
        .then(data => {
            data.clubs.forEach(club => {
                const clubRow = document.getElementById(club.name);
                if (clubRow) {
                    clubRow.cells[1].innerText = club.points;
                }
            });
        });
}
