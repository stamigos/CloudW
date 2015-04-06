$(document).ready(function() {

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

	formSubmit('.s-pb', '.photo-block');
	formSubmit('.s-uf-1', '.uf-1');
	formSubmit('.s-uf-2', '.uf-2');

	function formSubmit(button, form) {
		$( button ).click(function() {
			$( form ).submit();
		});
	}


});