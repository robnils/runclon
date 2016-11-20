/**
 * Created by rob on 2016-09-07.
 */
function bind_search_box(search_element_lname, search_element_fname, table_element_pending, table_element_registered) {

    $(search_element_lname).keyup(function () {
        // Search by last name
        var text = $(search_element_lname).val();
        //console.log(text);
        $(search_element_fname).val('');
        perform_search("search_by_last_name", text, table_element_pending, table_element_registered);
    });
    $(search_element_fname).keyup(function () {
        // Search by first name
        var text = $(search_element_fname).val();
        //console.log(text);
        $(search_element_lname).val('');
        perform_search("search_by_first_name", text, table_element_pending, table_element_registered);
    });

}

function perform_search(search_type, text, table_element_pending, table_element_registered) {
    console.log(text);
    if (text.length > 0) {
        console.log("Searching by " + search_type + " with " + text + "...");
        $.ajax({
            method: "POST",
            url: "/rcgeneral/" + search_type,
            data: {
                'text': text,
                'csrfmiddlewaretoken': get_csrf_token()
            }
        })
        .done(function (msg) {
            if (msg['success'] == true) {
                var registered = msg['registered'];
                var pending = msg['pending'];

                generate_table(table_element_pending, pending, false);
                generate_table(table_element_registered, registered, true);

                if(registered.length == 0) {
                    console.log('No results found for registered');
                    add_row_to_table(table_element_registered)
                }

                if(pending.length == 0) {
                    console.log('No results found for pending');
                    add_row_to_table(table_element_pending)
                }
                //swal({title: "Success", text: "Registered!", timer: 3000, type: "success"});
            } else {
                console.log("failed, clearing...");
                clear_table(table_id_pending);
                clear_table(table_id_registered);
                //swal({title: "Could not register user!", text: msg['reason'], timer: 3000, type: "error"});
            }
            //$(element).parent().parent().find(".glyphicon-refresh").hide();
        });
    } else {
        // Clear tables
        var table_id_pending = table_element_pending.attr('id');
        var table_id_registered = table_element_registered.attr('id');
        clear_table(table_id_pending);
        clear_table(table_id_registered);
    }
}

function clear_table(table_id) {
    //var table_id = table_element.attr('id');
    $("#" + table_id + " tbody tr").remove(); // Clear table
}
function generate_table(table_element, data, registered) {
    var table_id = table_element.attr('id');
    //clear_table(table_id);
    //console.log("#" + table_id + " tbody tr");
    //$("#" + table_id + " tbody tr").remove(); // Clear table
    clear_table(table_id);
    create_table(table_id, data, registered);
}

function add_row_to_table(table_element) {
    var table_id = table_element.attr('id');
    //var  tbl  = document.createElement('table');
    var tbl = document.getElementById(table_id);
    var tbody = tbl.getElementsByTagName('tbody')[0];
    var tr = tbody.insertRow();
    var td = tr.insertCell(0);
    td.appendChild(document.createTextNode('No results found'));
}

function create_table(table_id, data, registered){
    var body = document.body;
    //var  tbl  = document.createElement('table');
    var tbl = document.getElementById(table_id);
    var tbody = tbl.getElementsByTagName('tbody')[0];
    tbl.style.width  = '100%';
    tbl.style.border = '1px solid #ddd';

    var map_idx_to_key = {
        '0': 'id',
        '1': 'bib',
        '2': 'first_name',
        '3': 'last_name',
        '4': 'gender',
        '5': 'age_category',
        '6': 'club',
        '7': 'email',
        '8': 'number',
        '9': 'tshirt_size',
        '10': 'status',
        '11': 'registered_time'
    };
    for(var row_idx = 0; row_idx < data.length; row_idx++){
        var tr = tbody.insertRow();
        var dict = data[row_idx];
        console.log(dict);
        /*
        var map_idx_to_key = {};
        var index = 0;
        for(var key in dict) {
            map_idx_to_key[index] = key;
            index++;
        }*/

        // Add column
        for(var col_idx = 0; col_idx < Object.keys(dict).length; col_idx++){
            if(map_idx_to_key[col_idx] == 'registered_time' || map_idx_to_key[col_idx] == 'id') {
                continue;
            }

            var element = dict[map_idx_to_key[col_idx]];
            if(registered) {
               if(map_idx_to_key[col_idx] == 'status') {
                   var registered_time = remove_char_from_text(dict['registered_time'], ['T', 'Z']);
                   element += ' at ' + registered_time;
               }
            }

            var td = tr.insertCell(-1);
            td.appendChild(document.createTextNode(element));
            //td.style.border = '1px solid black';
            //td.style.width = '600px';
        }
        if(!registered) {
            // Register button
            //delete dict["registered_time"];
            //console.log(dict);
            var td = tr.insertCell(-1);
            var btn_id = 'register_button_' + dict['bib'];
            td.innerHTML = "<button class='btn-primary' id=" + btn_id + ">REGISTER</button>";
            bind_register_button(btn_id);
        }
    }
    body.appendChild(tbl);
}

function bind_register_button(btn_id) {
    $("#" + btn_id).click(function () {
        var bib = btn_id.split("register_button_")[1];
        register(bib);
    });
}

function register(bib) {
    var data = {
            'bib': bib,
            'csrfmiddlewaretoken': get_csrf_token()
    };
    $.ajax({
            method: "POST",
            url: "/rcgeneral/register",
            data: data
    })
    .done(function (msg) {
        if (msg['success'] == true) {
            location.reload();
            swal({title: "Success", text: "Registered!", timer: 3000, type: "success"});

        } else {
            location.reload();
            swal({title: "Could not register user!", text: msg['reason'], timer: 3000, type: "error"});
        }
        //$(element).parent().parent().find(".glyphicon-refresh").hide();

    });

}