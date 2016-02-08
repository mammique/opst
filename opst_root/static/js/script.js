// Piwik
  var _paq = _paq || [];
  _paq.push(["trackPageView"]);
  _paq.push(["enableLinkTracking"]);

  (function() {
    var u=(("https:" == document.location.protocol) ? "https" : "http") + "://opst.tetaneutral.net/piwik/";
    _paq.push(["setTrackerUrl", u+"piwik.php"]);
    _paq.push(["setSiteId", "1"]);
    var d=document, g=d.createElement("script"), s=d.getElementsByTagName("script")[0]; g.type="text/javascript";
    g.defer=true; g.async=true; g.src=u+"piwik.js"; s.parentNode.insertBefore(g,s);
  })();
// End Piwik Code

jQuery(document).ready(function() {
    
    $("#menu #menu-toggle a").on('click', function() {
        $("#menu li:not(#menu #menu-toggle)").toggle();
        $("#menu").toggleClass('expanded');
    });

    $("#col-left #col-left-toggle a").on('click', function() {
        $("#col-left > *:not(#col-left #col-left-toggle)").toggle();
        $("#col-left").toggleClass('expanded');
    });

    function window_resize() {

        // Hide the scroll bar to get actual viewport width.
        document.body.style.overflow = "hidden";
        var w = $(window).width();
        document.body.style.overflow = "";

        if(w > 991) {

            $("#menu li:not(#menu #menu-toggle)").css({'display': 'inline-block'});
            $("#col-left > *:not(#col-left #col-left-toggle)").css({'display': 'block'});
            $("#menu, #col-left").removeClass('expanded');

        } else {

            $("#menu li:not(#menu #menu-toggle)").css({'display': 'none'});
            $("#col-left > *:not(#col-left #col-left-toggle)").css({'display': 'none'});
        }
    }

    $(window).resize(window_resize);

/*   jQuery('.toggle').jTruncate({
		moreText: "[lire la suite]",
		length: 300,  
        minTrail: 10,   
        lessText: "[cacher texte]",  
        ellipsisText: "...",  
        moreAni: "fast",  
        lessAni: 300
	}); */
});
