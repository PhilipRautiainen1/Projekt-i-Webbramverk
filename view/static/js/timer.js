function changeButtons(){
    $('#next-question').css('cursor', 'pointer').attr('disabled', false);
    $('.answer').css('cursor', 'default').css({'background-color': 'red'}).removeAttr('onclick');
}

function Timer(){
    setTimeout(changeButtons, 15000)
    var i = 0;
    if (i == 0) {
    i = 1;
    var elem = document.getElementById("bar");
    var width = 1;
    var id = setInterval(frame, 150);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
        i = 0;
      } else {
        width++;
        elem.style.width = width + "%";
      }
    }
  }
}





