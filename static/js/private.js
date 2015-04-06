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

	//Script for chat functionality

	$('.send-ct').click(function() {
		appendMsg();
		resetTextareaValue('.inp-ct');
	});

	$('.inp-ct').keydown(function(e) {
		if (e.which == 13) {
			appendMsg();
			resetTextareaValue('.inp-ct');
		} else if (e.which == 32) {

		}
	});

	function appendMsg() {
		var msg = "<div class=\"msg-ct\"><div class=\"nickname-ct\">foo_bar</div><div class=\"date-ct\">"+ getSomeDate() +"</div><div class=\"msg-cont-ct\">" + $('.inp-ct').val() + "</div></div>";
		
		if ( $( '.inp-ct' ).val() ) {
			$('.users-messages-ct').prepend(msg);
		}
		
		function getSomeDate() {
			var months = [
				"Января", "Февраля", "Марта",
				"Апреля", "Мая", "Июня", "Июля",
				"Августа", "Сентября", "Октября",
				"Ноября", "Декабря"	
			];
			var date = new Date();
			var day = date.getDate();
			var monthIndex = date.getMonth();
			var month = months[monthIndex];
			var hours = date.getHours(); 
			var min = date.getMinutes(); 
			var time = day + " " + month + " " + "в" + " " + hours + ":" + min; 
			return time; 
		}
	}

	function resetTextareaValue( block ) {
		$( block ).val('');
	}

 //Script for hovering header icon "user"

  $('.user-h').on('mouseover', function (e) {
    e.stopPropagation();
    $(this).addClass('active-h');
    $('.drop-down').show(300);
  });

  $('html, body').on('mouseover', function () {
     $('.drop-down').hide(300);
     $('.user-h').removeClass('active-h').addClass('non-active-h');
  });

   $('.drop-down, .propagation').on('mouseover', function (e) {
      e.stopPropagation();
   });
});
