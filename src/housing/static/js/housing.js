$(document).ready(function() {
    
    //
    // Photo multiupload
    //
    
    $('#id_img').fileupload({
        url: add_photo_url,
	dataType: 'json',
        sequentialUploads: true,
        add: function (e, data) {

	    var jqXHR = data.submit()
		.success(function (result, textStatus, jqXHR) {
		    
		}).error(function (jqXHR, textStatus, errorThrown) {
		    console.log(jqXHR);
		}).complete(function (result, textStatus, jqXHR) {

		    $("#sortable").append(
			['<li data-id="',result.id,'" data-pos="',result.pos,'">',
			 '<div class="photo" data-id="',result.id,'">',
			 '<img src="',result.thumbnail,'" alt="',result.descr,'"/>',
			 '<label for="descr">Description</label><input id="descr" name="descr" data-type="set_photo_descr" data-id="',result.id,'" value="',result.descr,'" />',
			 '<button data-type="delete_photo" data-id="',result.id,'">Delete</button>',
			 '</div>',
			 '</li>'
			].join('')
		    );
		   
		    var overallProgress = $('#id_img').fileupload('progress');
		    per = Math.round(100*overallProgress.loaded/overallProgress.total);
		    if(per == 100) {
			$("#info").dialog("destroy");
			$("#info").remove();
		    }
		    else {
			$("#info").html(['<h3 style="text-align:center">Uploading: ',per,'%</h3>'].join(''));
		    }
		    

		});
        },
    }).bind('fileuploadstart', function(e, data) {
	console.log('start');
	$("body").append('<div id="info"></div>');
	$("#info").html('<h3 style="text-align:center">Uploading: 0%</h3>').dialog({
	    modal: true,
	    autoOpen: false,
	}).dialog("open");
	
    });
    
    
    //
    // Photo delete
    //
    
    $('body').on('click', "button[data-type=delete_photo]", function() {
	var id = $(this).data('id');
        var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
        $.post(delete_photo_url, {csrfmiddlewaretoken:csrfmiddlewaretoken, id:id}, function(data) {
            $("div").remove(".photo[data-id="+id+"]");
	    
	    // dialog box to validate deletion
	    /*
	    $("body").append('<div id="info"></div>');
            $("#info").html(data.content).dialog({
                modal: true,
                buttons: {
                    Ok: function() {
                        if(data.valid) {
                            $("div").remove(".photo[data-id="+id+"]");
                        }
                        $(this).dialog("destroy");
                    }
                }
            });*/
        }, 'json');
        return false;
    });
    
    $('body').on('change', "input[data-type=set_photo_descr]", function() {
        var id = $(this).data('id');
        var descr = $(this).val();
        var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
        $.post(set_photo_descr_url, {csrfmiddlewaretoken:csrfmiddlewaretoken, id:id, descr:descr});
        return false;
    });
    
    $("#sortable").sortable({
        'axis':'y',
        'update': function(event, ui) {
            var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
            var sort = $.extend({'csrfmiddlewaretoken':csrfmiddlewaretoken}, $("#sortable").sortable("toArray", {attribute:"data-id"}));
            
            $.post(sort_photo_url, sort, function(data) {
                
            });
        },
    });
    
    $('body').on('click', "button[data-type=add_room]", function() {
	var room_type = $("#id_room_type").val();
	var other_type = $("#id_other_type").val();
        var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
        $.post(add_room_url, {csrfmiddlewaretoken:csrfmiddlewaretoken, room_type:room_type, other_type:other_type}, function(data) {
            $("div[data-type=room]").html(data);
        });
        return false;
    });

    $('body').on('click', "button[data-type=delete_room]", function() {
	var user = $(this).data('user');
        var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
        $.post(delete_room_url, {csrfmiddlewaretoken:csrfmiddlewaretoken, user:user}, function(data) {
            $("div[data-type=room]").html(data);
        });
        return false;
    });

    $('body').on('click', "button[data-type=add_contributor]", function() {
	var user = $("#id_user").val();
        var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
        $.post(add_contributor_url, {csrfmiddlewaretoken:csrfmiddlewaretoken, user:user}, function(data) {
            $("div[data-type=contributor]").html(data);
        });
        return false;
    });

    $('body').on('click', "button[data-type=delete_contributor]", function() {
	var user = $(this).data('user');
        var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
        $.post(delete_contributor_url, {csrfmiddlewaretoken:csrfmiddlewaretoken, user:user}, function(data) {
            $("div[data-type=contributor]").html(data);
        });
        return false;
    });

    $("#accordion").accordion({
	heightStyle: "content",
	collapsible: true,
    });

    $('body').on('click', "button[data-type=update]", function() {
	
        var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
	var model = $(this).parent().attr("id");
	var form = $("#form").serializeArray();
	// form.push({name:'model', value:model});
	// form.push({name:'csrfmiddlewaretoken', value:csrfmiddlewaretoken});
	
	$.post(house_update_url, form, function(data) {

	});
	
	return false;
    });
});
