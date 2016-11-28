function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function updateLikes() {

    var ids = Array();

    $('.likes-count').each(function () {
        ids.push($(this).data('photo-id'));
    });

    $.getJSON('/photos/all/likes', {ids: ids.join(',')}, function (data) {
        for (var i in data['likes']) {
            $('.likes-count[data-photo-id=' + i + ']').html(data['likes'][i]);
        }

        for (var i in data['liked']) {
            if (data['liked'][i] == true) {
                $('.like[data-photo-id=' + i + ']').removeClass('fa-heart-o').addClass('fa-heart text-danger');
            } else {
                $('.like[data-photo-id=' + i + ']').removeClass('fa-heart text-danger').addClass('fa-heart-o');
            }
        }
    });
}