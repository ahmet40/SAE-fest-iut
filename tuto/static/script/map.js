
var map = L.map('map').setView([46.6031, 1.7348], 6); // Coordonnées du centre de la France

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Ajoutez vos coordonnées pour chaque région
var regions = {
    "Region1": [lat1, lon1],
    "Region2": [lat2, lon2],
    // ...
};

for (var region in regions) {
    var marker = L.marker(regions[region]).addTo(map);
    marker.bindPopup(region);
    marker.on('click', function(e) {
        var regionName = e.target.getPopup().getContent();
        // Envoyez regionName à votre serveur Flask pour traitement
        // Utilisez AJAX pour cela
        fetch('/get_region', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({region: regionName})
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.message);
        })
        .catch(error => console.error('Error:', error));
    });
}
