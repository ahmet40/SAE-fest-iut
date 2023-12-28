function search() {
    var query = document.querySelector('input[name="query"]').value.toLowerCase();
    var parcoursElements = document.querySelectorAll('.box-concert');
    var resultatMessage = document.getElementById('resultat-message');

    var anyResult = false; // Un drapeau pour indiquer s'il y a au moins un résultat

    parcoursElements.forEach(function(element) {
        var h3Text = element.querySelector('h3').textContent.toLowerCase();
        if (!h3Text.includes(query)) {
            element.style.display = 'none';
        } else {
            element.style.display = 'block';
            anyResult = true; // Il y a au moins un résultat
        }
    });

    // Afficher ou masquer le message en fonction des résultats
    if (anyResult) {
        resultatMessage.style.display = 'none';
    } else {
        resultatMessage.style.display = 'block';
    }
}
