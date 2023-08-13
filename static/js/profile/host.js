
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


    //스크롤시 헤더 이벤트
    $(window).scroll(function () {
        if ($(document).scrollTop() >= 100) {
            $header.css('background-color', '#fff').css('box-shadow', 'rgba(0, 0, 0, 0.15) 0px 0px 4px');
            $logoWhite.hide();
            $logoblack.show();
        }
        else {
            $header.css('background-color', 'transparent').css('box-shadow', 'none');
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
        if (!$(e.currentTarget).attr('class').includes('active-select')) {
            $product.toggleClass('active-select');
            $productBorder.toggleClass('active-product');
            $productCheck.toggleClass('active-check');
            $productCheckSvg.toggleClass('active-check-svg');
        }
    });
});
