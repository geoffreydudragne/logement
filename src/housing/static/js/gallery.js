//here I code a Jquery gallery

$(document).ready(function() {
    
    var photoContainer = $("#photoContainer"),
    bigPhoto = photoContainer.children("img"),
    thumbLinks = $("#thumbnails").find("a");
  
    thumbLinks.click(function(e){
      e.preventDefault();
      var $thisThumbLink = $(this),
        target = $thisThumbLink.attr("href");
      if (bigPhoto.attr("src") == target) return;
      //highlight($thisThumbLink);
      //photoContainer.html(loader);
        bigPhoto.load(function(){photoContainer.html($(this).fadeIn(250));}).attr("src",target);
    });
});
