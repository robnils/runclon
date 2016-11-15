/**
 * Created by rob on 2016-09-03.
 */

function fetch_statistics(url) {
    console.log('Fetching from ' + url + '...');
    $.ajax({
        method: "GET",
        url: url,
        data: {
            'csrfmiddlewaretoken': get_csrf_token()
        }
    })
    .done(function (msg) {
        if (msg['success'] == true) {
            //swal({title: "Success", text: "", timer: 3000, type: "success"});
            console.log(msg['stats']);
            return msg['stats'];

            //swal({title: "Success", text: "Registered!", timer: 3000, type: "success"});
        } else {
            //swal({title: "Could not register user!", text: msg['reason'], timer: 3000, type: "error"});
        }
        //$(element).parent().parent().find(".glyphicon-refresh").hide();
    });
    // $.ajax({
    //     type: 'GET',
    //     url: url,
    //     beforeSend: function() {
    //         // setting a timeout
    //         //$(placeholder).addClass('loading');
    //     },
    //     success: function(msg) {
    //         if (msg['success']) {
    //             //swal({title: "Success", text: "", timer: 3000, type: "success"});
    //             //return msg['stats'];
    //             return msg;
    //         } else {
    //             swal({title: "Not success", text: "!", timer: 3000, type: "error"});
    //         }
    //     },
    //     error: function(msg) {
    //         swal({title: "error", text: msg['reason'], timer: 3000, type: "error"});
    //     },
    //     complete: function() {
    //         //swal({title: "Complete!", text: "Registered!", timer: 3000, type: "success"});
    //     }
    // });
}

function poll_fetch_statistics(url) {
    setTimeout(function(){
         fetch_statistics(url);
    }, 30000);
}

