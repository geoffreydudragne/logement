var map = $('#map_canvas').gmap('get', 'map');

google.maps.event.addListener(map, "rightclick", function(event) {
    var lat = event.latLng.lat();
    var lng = event.latLng.lng();
    $('#latitude').val(lat);
    $('#longitude').val(lng);
});

$("centerButton").click(function(){

});
