$(document).ready(function () {
    $('#upload').on('change', function (event) {
        // Preview ảnh
        var upload_img = document.getElementById('image--upload');
        upload_img.src = URL.createObjectURL(event.target.files[0]);
        upload_img.onload = function () {
            URL.revokeObjectURL(upload_img.src); // Nhanh, free không tốn bộ nhớ 
        }
        // Tạo 1 form
        $('#femaleAlert').hide();
        $('#maleAlert').hide();
        var fd = new FormData();
        fd.append("upload", document.getElementById('upload').files[0]);
        $('#failAlert').text("Đang xử lý hình ảnh").show();
        $.ajax({
            url: '/upload', // -> views.upload
            contentType: false,
            processData: false,
            data: fd,
            type: 'post',
            // POST thành công
            success: function (response) {
                var predPath = './static/images/predict/' + response.img_name;
                var predict = response.predict;

                $('#femaleAlert').hide();
                $('#maleAlert').hide();
                $('#failAlert').hide();
                if (predict < 0) {
                    $('#failAlert').text("Lỗi: Ảnh không đạt yêu cầu").show();
                    $('#image--pred').attr('src', './static/images/resources/not-available.png');
                }
                else {
                    $('#image--pred').attr('src', predPath);
                    if (predict == 0) {
                        $('#maleAlert').text("Nam: " + response.correct * 100 + "%").show();
                    }
                    else if (predict == 1) {
                        $('#femaleAlert').text("Nữ: " + response.correct * 100 + "%").show();
                    }
                }
            }
        });
    });

});

$(".scrollToResult").click(function () {
    $('html,body').animate({
        scrollTop: ($("#result").offset().top - 56)
    },
        'slow');
});
