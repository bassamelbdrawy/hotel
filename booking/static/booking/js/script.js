
src ="http://code.jquery.com/jquery-1.11.0.min.js"
src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"
src="http%3A/code.jquery.com/jquery-1.11.0.min.js"
src="http://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js"
  $('.burger , .overlay').click(function(){
  $('.burger').toggleClass('clicked');
  $('.overlay').toggleClass('show');
  $('nav').toggleClass('show');
  $('body').toggleClass('overflow');
});
