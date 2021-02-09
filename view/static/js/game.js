let t;
let bar_handle;
let elem;
let i = 1;
let width = 1;

window.addEventListener('load', event => {
    bar_handle = setInterval(frame, 150);
    t = setTimeout(changeButtons, 15000);
    elem = document.getElementById("bar");
    console.log("starting");
});

function frame(){
    if (width >= 100) {
        clearInterval(bar_handle);
        i = 0;
    }
    else {
        width++;
        elem.style.width = width + "%";
    }
}

function changeButtons(){
    $('#next-question').css('cursor', 'pointer').attr('disabled', false);
    $('.answer').css('cursor', 'default').css({'background-color': 'red'}).removeAttr('onclick');
}

function reply(id){
    $.ajax({
        method:'POST',
        url:'http://127.0.0.1:5000/game',
        data: 'user_answer='+ id,
        crossDomain:true,

        success:(data)=>{
            if(data.response){
                $('#'+id).css({'background-color': 'green'});
                 for(i=0;i<3;i++) {
                     $('#'+id).fadeIn('fast', 0.5).fadeTo('fast', 1.0);
                 }
            }
            else {
                $('#answer'+data.correct).css({'background-color': 'green'}).fadeTo('slow', 0.5).fadeTo('slow', 1.0);
                $('#'+id).css({'background-color': 'red'});
                for(i=0;i<2;i++) {
                     $('#'+id).fadeTo('slow', 0.5).fadeTo('slow', 1.0);
                 }
            }
            $('#next-question').css('cursor', 'pointer').attr('disabled', false);
            $('.answer').css('cursor', 'default').removeAttr('onclick');
            clearTimeout(t);
            console.log(bar_handle);
            clearInterval(bar_handle);
            console.log(bar_handle);
    }});
}

function show_res(){
    $.ajax({
        method: 'GET',
        url: 'http://127.0.0.1:5000/end_game',

        success:(data)=>{
            $('#score').text(data.score);
            $('#correct').text(data.correct);
            $('#nr_quest').text(data.nr_quest);
        }
    })
    document.querySelector('#pop_bg').style.display = 'flex';
}