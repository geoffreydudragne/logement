$(document).ready(function() {

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
                    '<td>',item.name,'</td>',
                    '<td>',item.surface,'</td>',
                    '<td>',item.price,'</td>',
                    '<td><a href="',house_url.replace('0', item.id),'">See more</a>','</td>',
                    '</tr>'
                ].join(''));
            });
            
        });
        return false;
    });
});
