$(document).ready(function () {

  //Script for hovering header icon "user"

  $('.drop-down').css({'width': $('.propagation').innerWidth() + 'px'});

  $('.propagation').on('mouseover', function (e) {
    e.stopPropagation();
    $('.drop-down').show(50);
  });

  $('html, body').on('mouseover', function () {
     $('.drop-down').hide(300);
  });

   $('.drop-down, .propagation').on('mouseover', function (e) {
      e.stopPropagation();
   });

   //Script for submitting forms

  formSubmit('.b-cb', '.form-c');
  formSubmit('.cast', '.pass-cast');

  function formSubmit(button, form) {
    $( button ).click(function() {
      $( form ).submit();
    });
  }

  //Script for video block

  var tr = $('.table').find('tr');

  var vid = $('.videos-container').children();

  vid.css({'display':'none'});

  $(vid[0]).css({'display':'block'});

  for (var i=0; i < tr.length; i++) {
    tr[i].number = i;
  }

  var test = $('.bodies').find('.body-t');
  $(test[0]).css({'display':'block'});

  tr.click(function () {
    tr.removeClass('active-tr').css({'background-color':'#f1f1f1'});
    $(this).addClass('active-tr');
    tr.find('.active-drop').hide();
    $('.table')
              .find('.active-tr')
              .css({'background-color':'#ddd'})
              .find('.active-drop')
              .show();

    for (var k=0; k < vid.length; k++) {
      vid[k].pause();
    }

  vid.css({'display':'none'});
  $(vid[this.number]).css({'display':'block'});
  test.css({'display':'none'});
  $(test[this.number]).css({'display':'block'});

  });

 

  //Script for creating short message

  var more = $('.body-t').find('.more-t');

  for (var l=0; l < more.length; l++) {
    more[l].number = l;
  }

  var text = [];
  var textOpt = [];

  $('.text-a').each(function () {
    text.push($(this).html());
    var textS = $(this).html().substring(0, 250) + '...';
    textOpt.push(textS);
    $(this).html(textS);
  });

   more.on('click', function () {
    var block =  $('.bodies').find('.body-t');
    $(block[this.number]).find('.text-a').html(text[this.number]);
    $(this).css({'display':'none'});
   });


});