window.onload = function () {
    console.log("DOM loaded");
    $('a.remove-bas').on('click', function (event) {
        event.preventDefault();
        // console.log(event.target.href;
        $.ajax({
            url: event.target.href,
            success: function (data) {
                // console.log('response', data);
                $('.basket-item-' + data.training_basket_id).remove();
            }
        })

    })
}