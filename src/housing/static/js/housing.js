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
});
