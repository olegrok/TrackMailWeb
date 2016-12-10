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

$(document).ready(function () {
    $.getScript('/static/js/like-base.js');
    updateLikes();

    $('.like').click(function () {
        var url = $(this).data('likes-url');
        csrftoken = getCookie('csrftoken');
        var element = $(this);
        var params = {};
        params['vote-type'] = 1;
        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader("X-CSRFToken", csrftoken);
            },
            url: url,
            data: params,
            dataType: "json",
            success: function (data) {
                $('.likes-count[data-photo-id=' + element.data('photo-id') + ']').html(data);
                element.toggleClass('fa-heart-o fa-heart text-danger');

            }
        });
    });

    $('.edit-post-link').click(function () {
        $('#exampleModal').modal();
        $('.modal-body').load($(this).attr('href'));
        return false;
    });

    $(document).on('submit', '.ajax-post-edit-form', function () {
        var form = $(this);
        $.post(form.attr('action'), form.serialize(), function (data) {
            if (data == 'OK') {
                document.location.href = document.location.href;
            }
            form.html(data);
        });
    });

    window.setInterval(updateLikes, 5000);
});
