window.onload = function () {
    $('.order_container').on('click','input[type="number"]', function () {
        var t_href = event.target;
        var target_string = "/order/edit/" + t_href.name + "/" + t_href.value + "/";
        var order_pk = $('#order_number').val();
        console.log(t_href);
        console.log(target_string);
        console.log(order_pk);

        $.ajax({
            url: target_string,

            success: function (data) {
                $('.order_container').html(data.result);
            },
        });
        event.preventDefault();
    });
}
