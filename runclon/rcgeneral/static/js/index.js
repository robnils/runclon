/**
 * Created by rob on 2016-09-03.
 */

function fetch_statistics(url, callback) {
    console.log('Fetching from ' + url + '...');
    $.ajax({
        type: 'GET',
        url: url,
        beforeSend: function() {
            // setting a timeout
            //$(placeholder).addClass('loading');
        },
        success: function(msg) {
            if (msg['success']) {
                callback(msg['stats']);
            } else {
                console.log('Failed: '+ msg['reason']);
            }
        },
        error: function(msg) {
            swal({title: "error", text: msg['reason'], timer: 3000, type: "error"});
        },
        complete: function() {
            //swal({title: "Complete!", text: "Registered!", timer: 3000, type: "success"});
        }
    });
}

function refresh_ui(stats, $tot_part, $num_reg, $num_pending, $lat_reg) {
    if(stats != null) {
        console.log(stats);
        $tot_part.text(stats['total_participants']);
        $num_reg.text(stats['number_registered']);
        $num_pending.text(stats['number_not_registered']);
        $lat_reg.text(stats['latest_update']);
    } else {
        console.log('Could not refresh UI; stats='+stats);
    }

}

/*
* Polls the fetch_statistics method with an interval given in seconds as a parameter
*/
function poll_fetch_statistics(url, refresh_rate_in_seconds, ui_callback) {
    var rate_in_ms = refresh_rate_in_seconds * 1000;

    fetch_statistics(url, function (stats) {
        ui_callback(stats);
    });
    setTimeout(function () {
        poll_fetch_statistics(url, 3000, ui_callback);
    }, 3000);
}

