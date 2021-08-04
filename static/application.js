//reload the database contents once every three seconds
$(document).ready(function(){
    function refreshChat(){
        $.ajax({
            url: 'chat',
            type: 'GET',
            dataType: 'json',
            success: function(data){
                if(data.success){
                    let result = JSON.parse(data)
                    console.log(result)
                    $('#chatWindow').load('#chatWindow');
                }
            },
            error: function(data){console.log(data)}
        });
    }
    window.setInterval(refreshChat, 3000);
});