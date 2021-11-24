$('.js-sctipts-korsina').on('click', function(e) {
    e.preventDefault();
    $.ajax({
        url: e.target.href,
        success: function (data) {
            if (data.status){
                alert(data.message)
            }
            if (!data.status){
                alert(data.message)
            }
        }
    })
})