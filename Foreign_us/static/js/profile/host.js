let pay_item = "untact";

$(function () {
    // 객체들
    const $header = $('.header-container');
    const $logoWhite = $('.logo_hidden');
    const $logoblack = $('.logo_black');
    const $lessonBtn = $('.button-p');
    const $modal = $('.modal');
    const $modalBackground = $('.modal-background');
    const $payBtn = $('.pay-btn');
    const $product = $('div.product-item');
    const $productBorder = $('.product-border');
    const $productCheck = $('.product-check');
    const $productCheckSvg = $('.product-check-svg');
    const $loginBtn = $('.main-header-login-btn');


    //스크롤시 헤더 이벤트
    $(window).scroll(function () {
        if ($(document).scrollTop() >= 100) {
            $header.css('background-color', '#fff').css('box-shadow', 'rgba(0, 0, 0, 0.15) 0px 0px 4px');
            $loginBtn.css('background-color', '#333334').css('color', '#fff');
            $logoWhite.hide();
            $logoblack.show();
        }
        else {
            $header.css('background-color', 'transparent').css('box-shadow', 'none');
            $loginBtn.css('background-color', '#fff').css('color', '#333334');
            $logoWhite.show();
            $logoblack.hide();
        }
    });

    // 모달창 클릭 이벤트
    $lessonBtn.click(() => { $modal.show() });
    $modalBackground.click(() => { $modal.hide() });
    $payBtn.click(() => { $modal.hide() });

    // 과외 상품 클릭 이벤트
    $product.click((e) => {
        e.stopImmediatePropagation();
        if($(e.currentTarget).find(".product-select-input").attr('id') == "select-product"){
            pay_item = "contact";
            console.log(pay_item);
        } else{
            pay_item = "untact";
        }
        if (!$(e.currentTarget).attr('class').includes('active-select')) {
            $product.toggleClass('active-select');
            $productBorder.toggleClass('active-product');
            $productCheck.toggleClass('active-check');
            $productCheckSvg.toggleClass('active-check-svg');
        }
    });
});
