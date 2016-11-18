/**
 * Created by rob on 2016-09-07.
 */
function get_csrf_token() {
    var csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    return csrf;
}

/* From a given text, this function accepts a list of characters which are then remove from said text.
* The new subtext is then returned. */
function remove_char_from_text(text, split_list) {
    var subtext = text;
    var count = split_list.length;
    for(var idx = 0; idx < count; idx++) {
        var split_ch = split_list[idx];
        subtext = subtext.split(split_ch).join(' ');
    }
    return subtext;
}