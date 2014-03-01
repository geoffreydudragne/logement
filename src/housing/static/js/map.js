      $('#map_canvas').gmap().bind('init', function() { 
              // This URL won't work on your localhost, so you need to change it
              // see http://en.wikipedia.org/wiki/Same_origin_policy
              $.getJSON( STATIC_URL+'js/demo.json', function(data) { 
                  $.each( data.markers, function(i, marker) {
                      $('#map_canvas').gmap('addMarker', { 
                          'position': new google.maps.LatLng(marker.latitude, marker.longitude), 
                          'bounds': true 
                          }).click(function() {
                              $('#map_canvas').gmap('openInfoWindow', { 'content': marker.content }, this);
                              });
                      });
                  });
              });
