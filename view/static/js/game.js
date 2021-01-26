

function reply(id){
    $.ajax({
        method:'POST',
        url:'http://127.0.0.1:5000/game',
        data: 'user_answer='+ id,
        crossDomain:true,

        success:(data)=>{
            console.log($('#'+id).html())
            if(data.response){
                $('#'+id).css('border', '3px solid green');
            }
            else {
                $('#'+id).css('border', '3px solid red');
            }
            $('#next-question').html()
    }});
}

function check_answer(){
    pass
}
