function generate_table(table_element, data) {
    var table_id = table_element.attr('id');
    $("#" + table_id + " tbody tr").remove(); // Clear table
    tableCreate(table_id, data);
}

/**
 * Created by rob on 2016-09-07.
 */
function bind_search_box(search_element, table_element_not_registered, table_element_registered) {
    $(search_element).keyup(function () {
        var text = $(search_element).val();
        console.log(text);
        if (text.length > 0) {
            console.log("searching " + text + "...");
            $.ajax({
                method: "POST",
                url: "/rcgeneral/search",
                data: {
                    'text': text,
                    'csrfmiddlewaretoken': get_csrf_token()
                }
            })
                .done(function (msg) {
                    if (msg['success'] == true) {
                        var registered = msg['registered'];
                        var not_registered = msg['not_registered'];
                        //generate_table(table_element, not_registered, registered);
                        console.log(not_registered);
                        if(not_registered.length > 0) {
                            generate_table(table_element_not_registered, not_registered);
                        }
                        if(registered.length > 0) {
                            generate_table(table_element_registered, registered);
                        }
                        //swal({title: "Success", text: "Registered!", timer: 3000, type: "success"});
                    } else {
                        //swal({title: "Could not register user!", text: msg['reason'], timer: 3000, type: "error"});
                    }
                    //$(element).parent().parent().find(".glyphicon-refresh").hide();
                });
        }
    });
}

function tableCreate(table_id, data){
    var body = document.body;
    //var  tbl  = document.createElement('table');
    var tbl = document.getElementById(table_id);
    tbl.style.width  = '500px';
    tbl.style.border = '1px solid #ddd';

    for(var row_idx = 0; row_idx < data.length; row_idx++){
        var tr = tbl.insertRow();

        var dict = data[row_idx];

        var map_idx_to_key = {};
        var index = 0;
        for(var key in dict) {
            map_idx_to_key[index] = key;
            index++;
        }

        for(var col_idx = 0; col_idx < Object.keys(dict).length; col_idx++){
            var td = tr.insertCell();
            td.appendChild(document.createTextNode(dict[map_idx_to_key[col_idx]]));
            td.style.border = '1px solid black';
        }
    }
    body.appendChild(tbl);
}