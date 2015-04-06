$( document ).ready(function () {

  $('.b-ft').click(function() {
    $(this).parent().css({'display':'none'});
    $('.clicked-b-ft').fadeIn(500);
  });

  $('.go-back-g').click(function() {
    $('.non-clicked-b-ft').css({'display':'block'});
    $('.clicked-b-ft').fadeOut(0);
  });

  //Script for submitting forms

  formSubmit('.submit-gf', '.greet-form');
  formSubmit('.b-bh', '.inputs-bh');

  function formSubmit(button, form) {
    $( button ).click(function() {
      $( form ).submit();
    });
  }



});