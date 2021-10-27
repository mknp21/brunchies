// import { MarkerClusterer } from "@googlemaps/markerclusterer";

let map;
let markers = [];


function initMap() {
    const sfCoords = {
        lat: 37.7749,
        lng: -122.4194,
    };

    const mapOptions = {
        scrollwheel: false,
        zoom: 13,
        center: sfCoords,
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
    };

    map = new google.maps.Map(document.querySelector('#map'), mapOptions);
    
    // const labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    // const locations = [];
    // $.get('/restinfo.json', res => {
    //     console.log("get reqest made, response stuff")
    //   for (const restaurant of res.results) {
    //     locations.push({'lat': Number(restaurant.lat), 'lng': (restaurant.long)})
    // }});

    // const markers = locations.map((location, i) => {
    //     // console.log("location is ", location)
    //     return new google.maps.Marker({
    //       position: location,
    //       label: labels[i % labels.length],
    //     });
    //   });
    
    //   console.log({markers})
    
    // pins all restaurants to the map
    // const markers = $.get('/restinfo.json', res => {
    //     for (const restaurant of res.results) {

    //         const placeCoords = new google.maps.LatLng(Number(restaurant.lat), Number(restaurant.long));
    
    //         new google.maps.Marker({
    //             position: placeCoords,
    //             title: restaurant.name,
    //             map: map,
    //             icon: "/static/img/pink-pushpin.png"
    //         });
    //     };
    // });

    // const markers = []

    // REMEMBER THIS WORKS!!!
    $.get('/restinfo.json', res => {
      for (const restaurant of res.results) {

        const placeCoords = new google.maps.LatLng(Number(restaurant.lat), Number(restaurant.long));
    
        markers.push(new google.maps.Marker({
            position: placeCoords,
            title: restaurant.name,
            map: map,
            icon: "/static/img/pink-pushpin.png"
        }));
      };
    });

    const markerCluster = new markerClusterer.MarkerClusterer({ map, markers });

}

// REMEMBER THIS WORKS!!!
window.initMap = initMap;

// may or may not need this here
// const locations = [];
// $.get('/restinfo.json', res => {
//     console.log("int he external get")
//     for (const restaurant of res.results) {
//         locations.push({'lat': Number(restaurant.lat), 'lng': (restaurant.long)})
//     }});









// ignore everything below this line
// function addMarkers() {
//     $.get('/restinfo.json', res => {
//         const locations = [];
//         for (const restaurant of res.results) {
//             locations.push({'name': restaurant.name, 'lat': Number(restaurant.lat), 'lng': (restaurant.long)})
//         };

//         locations.forEach(center => {
//             markers.push(new google.maps.Marker({
//                 position: {lat: center.lat, lng: center.lng},
//                 map: null,
//                 title: center.name,
//                 icon: "/static/img/pink-pushpin.png"
//             }));
//         });
//         drawMarkerClusterer();
//     });
// }

// function drawMarkerClusterer() {
//     let brunchCluster = new MarkerClusterer(
//         this.map,
//         markers,
//     );
// };

// window.initMap = initMap;


