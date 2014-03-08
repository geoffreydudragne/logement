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
            $("#sortable").sortable({
                'axis':'y',
                'update': function(event, ui) {
                    var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
                    var sort = $.extend({'csrfmiddlewaretoken':csrfmiddlewaretoken}, $("#sortable").sortable("toArray", {attribute:"data-id"}));
                    $.post(sort_photo_url, sort);
                },
            });
        });
        // $("#info").dialog("close");
    });
    /*
      .bind('fileuploadstart', function (e, data) {
      $("body").append('<div id="info"></div>');
      $("#info").html('Uploading').dialog({
      modal: true,
      autoOpen: false,
      }).dialog("open");
      });
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
            console.log(sort);
            $.post(sort_photo_url, sort, function(data) {
                
            });
        },
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
});
