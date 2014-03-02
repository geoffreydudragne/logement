$(document).ready(function() {
    $("#add_photo").unbind().on('click', function() {
        $.get('/housing/house/add_photo/1', function(data) {
            $("body").append('<div id="test"></div>');
            $("#test").html(data).dialog({
                width:800,
                height:600,
                buttons: {
                    Add: function() {
                        var form = $("#test form").serialize();
                        $.post('/housing/house/add_photo/1', form, function(data) {
                            $("#test").html(data);
                        });
                    }
                }
            });
        });
        return false;
    });
});
