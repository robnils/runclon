/**
 * Created by rob on 2016-09-07.
 */
function bind_search_box(search_element, table_element) {
    $(search_element).keydown(function () {
        var text = $(search_element).val();
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
                        console.log(msg['registered']);
                        console.log(msg['not_registered']);
                        var registered = msg['registered'];
                        var not_registered = msg['not_registered'];
                        generate_table(table_element, not_registered, registered);
                        //swal({title: "Success", text: "Registered!", timer: 3000, type: "success"});
                    } else {
                        //swal({title: "Could not register user!", text: msg['reason'], timer: 3000, type: "error"});
                    }
                    //$(element).parent().parent().find(".glyphicon-refresh").hide();
                });
        }
    });
}

function generate_table(table_element, not_registered, registered) {
    //var table_id = table_element.attr('id');
    //$("#" + table_id + " tbody tr").remove(); // Clear table
    //tableCreate();
    for(var idx in not_registered) {
        console.log(not_registered[idx]);
        table_element.after('<tr>asd</tr>');
        //$('#myTable tr:last').after('<tr>asd</tr>');

        //table_element.innerHTML("")
    }

}

function tableCreate(){
    var body = document.body,
        tbl  = document.createElement('table');
    //var tbl = document.getElementById(table_id);
    tbl.style.width  = '100px';
    tbl.style.border = '1px solid black';

    for(var i = 0; i < 3; i++){
        var tr = tbl.insertRow();
        for(var j = 0; j < 2; j++){
            if(i == 2 && j == 1){
                break;
            } else {
                var td = tr.insertCell();
                td.appendChild(document.createTextNode('Cell'));
                td.style.border = '1px solid black';
                if(i == 1 && j == 1){
                    td.setAttribute('rowSpan', '2');
                }
            }
        }
    }
    body.appendChild(tbl);
}