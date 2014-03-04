$(document).ready(function() {
    $("#add_photo").unbind().on('click', function() {
	$.get(add_photo_url, function(data) {
            $("body").append('<div id="test"></div>');
            $("#test").html(data).dialog({
                width:800,
                height:600,
                buttons: {
                    Add: function() {
                        var form = $("#test form").serialize();
                        $.post(add_photo_url, form, function(data) {
                            $("#test").html(data);
                        });
                    }
                }
            });
        });
        return false;
    });
    
    $("button[data-type=delete_photo]").on('click', function() {
	var id = $(this).data('id');
        var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
        console.log(csrfmiddlewaretoken);
        $.post(delete_photo_url, {csrfmiddlewaretoken:csrfmiddlewaretoken, id:id}, function(data) {
            $("body").append('<div id="info"></div>');
            $("#info").html(data.content).dialog({
                modal: true,
                buttons: {
                    Ok: function() {
                        $("#info").dialog("close");
                        $("#info").dialog("destroy");
                    }
                }
            });
            if(data.valid) {
                console.log($("div[data-id="+id+"]"));
                $("div").remove(".photo[data-id="+id+"]");
            }
        }, 'json');
        return false;
    });
});
