(function($){
	$('.picker .actions').css({'position':'absolute','left':-9999});
	$('.picker label').append($('<button type="button">Pick</button>'));
	$('.picker button').click(function(){
		$(this).parents('label').find('input').attr('selected', 'selected');
	});
	$('.picker form').change(function(){
		$(this).submit();
	})
})(jQuery)