$(document).ready(function() {
    
    //
    // Photo multiupload
    //
    
    $('#id_img').fileupload({
        dataType: 'json',
        sequentialUploads: true,
        add: function (e, data) {
            data.submit();
        },
    }).bind('fileuploadstop', function (e, data) {
        // when upload is done, we refresh the content
        // get is done only once
        $.get(get_photo_url, function(data) {
            $("div[data-type=photo]").html(data);
            $("#sortable").sortable();
        });
    });
    
    /*
      .bind('fileuploadstart', function (e, data) {
        $("body").append('<div id="info"></div>');
        $("#info").html('<div id="progressbar"></div>').dialog({
            modal: true,
            buttons: {
                Ok: function() {
                    if(data.valid) {
                        $("div").remove(".photo[data-id="+id+"]");
                    }
                }
            }
        }).dialog("open");
        $("#progressbar").progressbar({
            value: 0
        });
    }).bind('fileuploadprogress', function (e, data) {
        var progress = parseInt(data.loaded / data.total * 100, 10);
        $("#progressbar").progressbar("value", progress);
        console.log(progress);
    })
    
     */

    
    //
    // Photo delete
    //
    
    $('body').on('click', "button[data-type=delete_photo]", function() {
	var id = $(this).data('id');
        var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
        $.post(delete_photo_url, {csrfmiddlewaretoken:csrfmiddlewaretoken, id:id}, function(data) {
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
            });
        }, 'json');
        return false;
    });

    $("#sortable").sortable({
        'axis':'y',
        'update': function(event, ui) {
            var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
            var sort = $.extend({'csrfmiddlewaretoken':csrfmiddlewaretoken}, $("#sortable").sortable("toArray", {attribute:"data-id"}));
            console.log(sort);
            $.post(sort_photo_url, sort, function(data) {
                
            });
        },
    });
});
