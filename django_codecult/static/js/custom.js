function textToList(text) {
	return text.split(',');
}

$(".slider-button").click(function(){
	// Get source of image corresponding to selected button
	var src = $(this).find('img').attr('src');
	// Get id of clicked button
	var id = $(this).attr('id');
	// Get primary key of image slider object
	var pk = id.split('-')[1];
	// Change the source of the displayed image
	$('#image-visible-'.concat(pk)).find('img').attr('src', src);
	// Get the class corresponding to the previous button id
	var old_id = $('#image-visible-'.concat(pk)).attr('class');
	// Change shown image class to the new id
	$('#image-visible-'.concat(pk)).attr('class', id);
	// Change the old button to the 'not-selected' class
	$('#'+old_id).attr('class', 'not-selected slider-button');
	// Add class 'selected-button' to this button
	$(this).attr('class', 'selected-button slider-button');
})

$(document).ready(function(){
	$('#0').attr('class', 'selected-button slider-button');
})