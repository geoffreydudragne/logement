$(document).ready(function() {

    var map = $('#map_canvas').gmap('get', 'map');
    var geocoder = new google.maps.Geocoder();

    google.maps.event.addListener(map, "click", function(event) {
        var lat = event.latLng.lat();
        var lng = event.latLng.lng();
        $('#id_latitude').val(lat);
        $('#id_longitude').val(lng);
        $('#map_canvas').gmap('clear', 'markers');
        $('#map_canvas').gmap('addMarker', { 
            'position': new google.maps.LatLng(lat, lng)
        });
    });

    //$("#centerButton").click(function(){
    $("#ui-accordion-accordion-header-4").click(function(){
        //geocoder.geocode( { 'address': $('#address').val()}, function(results, status) { // test version
        geocoder.geocode( { 'address': $('#id_address').val()+', '+ $('#id_city').val()}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                map.setCenter(results[0].geometry.location);
                $('#map_canvas').gmap('option', 'zoom', 19);
                $('#map_canvas').gmap('option', 'mapTypeId', google.maps.MapTypeId.SATELLITE);
                $('#map_canvas').gmap('addMarker', { 'position': results[0].geometry.location });
            }
        });
    });
});
