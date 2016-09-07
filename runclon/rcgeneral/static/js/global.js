/**
 * Created by rob on 2016-09-07.
 */
function get_csrf_token() {
    var csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    return csrf;
}