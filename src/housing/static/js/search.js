$(document).ready(function() {

    $('#map_canvas').gmap({ 'center': '43.614252,7.072984' }).gmap('option', 'zoom', 11);
    $('#map_canvas').gmap('addMarker', {
        'position': new google.maps.LatLng(43.614252,7.072984),
        'icon': new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=E|239CD3|000000")
    }).click(function() {
        $('#map_canvas').gmap('openInfoWindow', {'content': "Eurecom"}, this);
    });

    $('#search').on('click', function() {

        var get_string = search_url;
        var name, value, fields;
        first = true;
        // Construction of the GET request string
        $("input").each(function() {
            name = this.name;
            value = this.value;
            if(this.type=="checkbox") {
                if(this.checked) {
                    value = "True";
                }
                else {
                    value = false;
                }
            }
            
            if(value) {
                if(first) {
                    get_string += '?'+name+'='+value;
                    first = false;
                }
                else {
                    get_string += '&'+name+'='+value;
                }
            }
        });
        
	$("select").each(function() {
            name = this.name;
            value = $(this).val();
            
            if(value) {
                if(first) {
		    get_string += '?'+name+'='+value;
		    first = false;
                }
                else {
		    get_string += '&'+name+'='+value;
                }
	    }
        });
	
        $.getJSON(get_string, function(data) {
            $("#house_list table tbody").html("");
            $.each(data, function(i, item) {
                $("#house_list table tbody").append([
                    '<tr>',
                    '<td><a href="',house_url.replace('0', item.id),'">',item.name,'</a></td>',
                    '<td>',item.surface,'</td>',
                    '<td>',item.price,'</td>',
                    '</tr>'
                ].join(''));

                $('#map_canvas').gmap('addMarker', { 
                    'position': new google.maps.LatLng(item.latitude, item.longitude),
                    'icon': new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld="+ item.result_rank +"|F85850|000000")
                }).click(function() {
                    $('#map_canvas').gmap('openInfoWindow', { 'content': item.name }, this);
                });
            });
            
        });
        return false;
    });
});
