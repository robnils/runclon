/**
 * Created by rob on 2016-09-03.
 */

function add_registration(data) {
    // TODO refactor to http://kyleschaeffer.com/development/the-perfect-jquery-ajax-request/
    data['csrfmiddlewaretoken'] = get_csrf_token();
    $("#add").prop('disabled', true);
    $.ajax({
            method: "POST",
            url: "/rcgeneral/add",
            data: data
        })
        .done(function (msg) {
            if (msg['success'] == true) {
                swal({title: "Success", text: "Added!", timer: 3000, type: "success"});
            } else {
                swal({title: "Could not add user!", text: msg['reason'], timer: 3000, type: "error"});
            }
            //$(element).parent().parent().find(".glyphicon-refresh").hide();
        });
    $("#add").prop('disabled', false);
}

function get_registrations() {
    $("#view_registrations").addClass("error");
    $.ajax({
            method: "GET",
            url: "/rcgeneral/get_registrations"
        })
        .done(function (msg) {
            if (msg['success'] == true) {
                var registrations = msg['registrations'];
                for (var lst_idx = 0; lst_idx < registrations.length; lst_idx++) {
                    console.log(registrations[lst_idx]);
                }
                display_registrations(registrations);
            } else {
                swal({title: "Could not get registrations!", text: msg['reason'], timer: 3000, type: "error"});
                return null;
            }
        });
    $("#view_registrations").prop('disabled', false);
}

function clear_all() {
    $("#clear_all").prop('disabled', true);
    $.ajax({
            method: "GET",
            url: "/rcgeneral/clear_all"
        })
        .done(function (msg) {
            if (msg['success'] == true) {
                swal({title: "Done!", text: "Successfully removed all registrations!", timer: 3000, type: "success"});
            } else {
                swal({title: "Could not get registrations!", text: msg['reason'], timer: 3000, type: "error"});
                return null;
            }
        });
    $("#clear_all").prop('disabled', false);
}
function register(data) {
    data['csrfmiddlewaretoken'] = get_csrf_token();
    $("#add").prop('disabled', true);
    $.ajax({
            method: "POST",
            url: "/rcgeneral/register",
            data: data
        })
        .done(function (msg) {
            if (msg['success'] == true) {
                swal({title: "Success", text: "Registered!", timer: 3000, type: "success"});
            } else {
                swal({title: "Could not register user!", text: msg['reason'], timer: 3000, type: "error"});
            }
            //$(element).parent().parent().find(".glyphicon-refresh").hide();
        });
    $("#add").prop('disabled', false);
}
function display_registrations(data) {
    var table = $('<table></table>').addClass('');
    for (var row_idx = 0; row_idx < data.length; row_idx++) {
        var row_txt = "";
        var dict = data[row_idx];
        for (var key in dict) {
            row_txt += dict[key] + "\t";
        }
        var row = $('<tr></tr>').addClass('').text(row_txt);
        table.append(row);
    }
    $('#results').append(table);
}
// Bindings
function bind_view_button() {
    $("#view_registrations").click(function () {
        get_registrations();
    });
}

function bind_clear_all_button() {
    $("#clear_all").click(function () {
        clear_all();
    });
}

function bind_add_button() {
    $("#add").click(function () {
        var data = {
            'bib': $("#bib").val(),
            'first_name': $("#first_name").val(),
            'surname': $("#surname").val(),
            'gender': $("#gender").val(),
            'age_category': $("#age_category").val(),
            'club': $("#club").val(),
            'email': $("#email").val(),
            'number': $("#number").val()
        };
        console.log(data);
        add_registration(data);
    });
}

function bind_register_button() {
    $("#register").click(function () {
        var data = {
            'bib': $("#bib").val()
        };
        register(data);
    });
}