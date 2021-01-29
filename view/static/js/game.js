

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
    }});
}

function check_answer(){
    pass
}
