'use strict';

let map;

function initMap() {
    const sfCoords = {
        lat: 37.7749,
        lng: -122.4194,
    };
    
    map = new google.maps.Map(document.querySelector('#map'), {
        center: sfCoords,
        zoom: 12,
    });

    $.get('/save-data.json', res => {
        for (const restaurant of res.results) {
    
            // const placeCoords = {
            //     lat: Number(restaurant.lat),
            //     long: Number(restaurant.long)
            // };

            const placeCoords = new google.maps.LatLng(Number(restaurant.lat), Number(restaurant.long));
    
            new google.maps.Marker({
                position: placeCoords,
                title: restaurant.name,
                map: map,
            });
        };
    });
}



// let savedItem = $('#saved-item');

// savedItem.on('mouseover', () => {
//     alert('Works!');
// });

// $('#saved-item').on('mouseover', () => {
//     $.post('/saved', res => {
//         alert(res)
//     })
// })

// $.post('/saved', response => {
//     const savedCoord = {
//         latitude:
//         longitude:
//     }
// })