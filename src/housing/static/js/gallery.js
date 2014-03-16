//here I code a Jquery gallery

$(document).ready(function() {
    
    photoContainer = $("#photoContainer");
    bigPhoto = photoContainer.children("img");
    thumbList = $("#thumbnails");
    thumbLinks = thumbList.find("a");
    thumbnails = thumbList.find("img");
    $("#thumbnail0").addClass("active");
    previousButton=$("#previousButton")[0];
    nextButton=$("#nextButton")[0];
    previousButton.disabled=true;
    nextButton.disabled=false;

    loader = $(document.createElement("img")).attr({
      alt: "chargement en cours",
      title: "chargement en cours",
      src: STATIC_URL+"img/loader.gif",
      id: "loader"
    });
  
/*    thumbLinks.click(function(e){
      e.preventDefault();
      var $thisThumbLink = $(this);
      var target = $thisThumbLink.attr("href");
      if (bigPhoto.attr("src") == target) return;
      //highlight($thisThumbLink);
      photoContainer.html(loader);
      bigPhoto.load(function(){photoContainer.html($(this).fadeIn(250));}).attr("src",target);
    });
}); */

});

function loadphoto(photoNumber){

    var target = photoRef[photoNumber];
    if (bigPhoto.attr("src") == target) return;

    current=photoNumber;
    scrollLevel=(photoNumber-4)*110;
    thumbnails.removeClass("active");
    $("#thumbnail"+photoNumber).addClass("active");

    bigPhoto.css("opacity",1);
    photoContainer.html(loader);
    bigPhoto.load(function(){
        photoContainer.html($(this).fadeIn(250, function(){
            photoContainer.append('<div id="photoDescr">'+photoDescr[photoNumber]+'</div>');}))
    }).attr("src",target).attr("alt",photoDescr[photoNumber]);

    if (photoNumber==0) {
        previousButton.disabled=true;
    }
    else {
        previousButton.disabled=false;
        $.cacheImage(photoRef[photoNumber-1]);                   
    }
    
    if (photoNumber==numberphotos-1) {
        nextButton.disabled=true;
    } 
    else {
        nextButton.disabled=false;
        $.cacheImage(photoRef[photoNumber+1]);                   
    }
}

var current=0;
var scrollLevel=-440;

function loadPrevious(){
    current--;
    loadphoto(current);

    scrollLevel-=110;
    thumbList.scrollLeft(scrollLevel);
}

function loadNext(){
    current++;
    loadphoto(current);

    scrollLevel+=110;
    thumbList.scrollLeft(scrollLevel);
}

$.cacheImage(photoRef[1]);                   
