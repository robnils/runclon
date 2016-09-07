/**
 * Created by rob on 2016-09-07.
 */
function bind_search_box(element) {
    $(element).keydown(function() {
        var text = $(element).val();
        if(text.length > 3) {
            console.log("searching " + text + "...");
            $.ajax({
                method: "POST",
                url: "/rcgeneral/search",
                data: data
            })
            .done(function (msg) {
                if (msg['success'] == true) {
                    console.log(msg['results']);
                    //swal({title: "Success", text: "Registered!", timer: 3000, type: "success"});
                } else {
                    //swal({title: "Could not register user!", text: msg['reason'], timer: 3000, type: "error"});
                }
                //$(element).parent().parent().find(".glyphicon-refresh").hide();
            });
        }
    });
}