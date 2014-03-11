//here I code a Jquery gallery

$(document).ready(function() {
    
    photoContainer = $("#photoContainer");
    bigPhoto = photoContainer.children("img");
    thumbLinks = $("#thumbnails").find("a");
    thumbnails = $("#thumbnails").find("img");
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

function loadImage(imageNumber){

    var target = imageRef[imageNumber];
    if (bigPhoto.attr("src") == target) return;

    if (imageNumber==0) {previousButton.disabled=true;} else {previousButton.disabled=false;}
    if (imageNumber==numberImages-1) {nextButton.disabled=true;} else {nextButton.disabled=false;}

    current=imageNumber;
    thumbnails.removeClass("active");
    $("#thumbnail"+imageNumber).addClass("active");

    photoContainer.html(loader);
    bigPhoto.load(function(){photoContainer.html($(this).fadeIn(250));}).attr("src",target).attr("alt",imageDesc[imageNumber]);
}

var current=0;

function loadPrevious(){
	current--;
		loadImage(current);
}

function loadNext(){
	current++;
		loadImage(current);
}

