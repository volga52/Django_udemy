window.onload = function () {
    $('.basket_list').on('click','input[type="number"]', function () {
        var t_href = event.target;
        var t_string = "/basket/edit/" + t_href.name + "/" + t_href.value + "/";
        console.log(t_href);

        $.ajax({
            url: t_string,

            success: function (data) {
                $('.basket_list').html(data.result);
            },
        });
        event.preventDefault();
    });
}
