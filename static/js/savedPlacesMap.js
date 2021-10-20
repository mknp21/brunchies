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
        styles: [
            {
                "featureType": "administrative.country",
                "elementType": "geometry.stroke",
                "stylers": [
                    {
                        "lightness": -5
                    },
                    {
                        "color": "#b0b0b0"
                    },
                    {
                        "weight": 1.7
                    }
                ]
            },
            {
                "featureType": "administrative.province",
                "elementType": "all",
                "stylers": [
                    {
                        "visibility": "off"
                    }
                ]
            },
            {
                "featureType": "landscape",
                "elementType": "geometry",
                "stylers": [
                    {
                        "color": "#ddc0b4"
                    },
                    {
                        "lightness": 26
                    }
                ]
            },
            {
                "featureType": "poi",
                "elementType": "geometry",
                "stylers": [
                    {
                        "color": "#ddc0b4"
                    }
                ]
            },
            {
                "featureType": "road.highway",
                "elementType": "all",
                "stylers": [
                    {
                        "color": "#ddc0b4"
                    }
                ]
            },
            {
                "featureType": "road.arterial",
                "elementType": "all",
                "stylers": [
                    {
                        "visibility": "off"
                    }
                ]
            },
            {
                "featureType": "road.local",
                "elementType": "all",
                "stylers": [
                    {
                        "visibility": "off"
                    }
                ]
            },
            {
                "featureType": "transit",
                "elementType": "all",
                "stylers": [
                    {
                        "visibility": "off"
                    }
                ]
            },
            {
                "featureType": "water",
                "elementType": "geometry",
                "stylers": [
                    {
                        "color": "#ddc0b4"
                    },
                    {
                        "lightness": 66
                    }
                ]
            }
        ]
    });

    $.get('/save-data.json', res => {
        for (const restaurant of res.results) {

            const placeCoords = new google.maps.LatLng(Number(restaurant.lat), Number(restaurant.long));
    
            new google.maps.Marker({
                position: placeCoords,
                title: restaurant.name,
                map: map,
                icon: "/static/img/pink-pushpin.png"
            });
        };
    });
}

