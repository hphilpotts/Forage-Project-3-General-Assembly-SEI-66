
$( ".pic" ).hover(
    function() {
      $( this ).append( $( "<span> ***</span>" ) );
    }, function() {
      $( this ).find( "span" ).last().remove();
    }
  );
   
  $( ".pic.fade" ).hover(function() {
    $( this ).fadeOut( 100 );
    $( this ).fadeIn( 500 );
  });