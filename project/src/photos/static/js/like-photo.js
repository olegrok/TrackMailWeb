function updatePhotoLikes() {
    $.getJSON($('.like').data('likes-url'), function (data) {
        $('.likes-count').html(data['likes']);

        if (data['liked'] == true) {
            $('.like').removeClass('fa-heart-o').addClass('fa-heart text-danger');
        } else {
            $('.like').removeClass('fa-heart text-danger').addClass('fa-heart-o');
        }
    });
}

$(document).ready(function () {
    $.getScript('/static/js/like-base.js');
    updatePhotoLikes();

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

    window.setInterval(updatePhotoLikes, 5000);

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
            // else {
            //
            // }
            form.html(data);
        });
    });

});
