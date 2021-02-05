function changeButtons(){
    $('#next-question').css('cursor', 'pointer').attr('disabled', false);
    $('.answer').css('cursor', 'default').css({'background-color': 'red'}).removeAttr('onclick');
}

function Timer(){
    setTimeout(changeButtons, 15000)
}