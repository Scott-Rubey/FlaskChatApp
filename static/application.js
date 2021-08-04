//reload the database contents once every three seconds
/*
$(document).ready(function() {
    $.ajax({
        url: "chat",
        type: "GET",
        dataType: "json",
        success: function (data) {
            if (data.success) {
                console.log(data)
                $('#chatWindow').load(data)
            }
        },
        error: function (request, error) {}
    });
}, 3000);
*/
$(document).ready(function(){
    function refreshChat(){
        $.ajax({
            url: 'chat',
        }).done(function(result) {
            $('#chatWindow').load();
        });
    }
    window.setInterval(refreshChat, 3000);
});