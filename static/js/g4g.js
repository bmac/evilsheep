$(document).ready(
    function () {
        //Searchbox2 show/hide default text if needed
        //global vars
        var searchBox = $("#s");
        var searchBoxDefault = "Search...";

        searchBox.focus(function(){
                            if($(this).attr("value") == searchBoxDefault) $(this).attr("value", "");
                        });
        searchBox.blur(function(){
                           if($(this).attr("value") == "") $(this).attr("value", searchBoxDefault);
                       });


    });
