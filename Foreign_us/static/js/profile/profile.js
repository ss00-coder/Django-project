let pay_item = "untact";

$(function () {
    // 객체들
    const $header = $('.header-container');
    const $logoWhite = $('.logo_hidden');
    const $logoblack = $('.logo_black');
    const $tabBtn = $('.title-button');
    const $introduction = $('.introduction');
    const $reviewWrapper = $('.review-wrapper');
    const $postsWrapper = $('.posts-wrapper');
    const $snsWrapper = $('.sns-wrapper');
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


    // 탭 버튼 이벤트
    $tabBtn.click((e) => {

        // 소개 탭 누를시 이벤트
        if ($(e.currentTarget).text().includes('소개')) {
            if (!$(e.currentTarget).attr('class').includes('active-tab')) {
                $('.tab-line').remove();
                $('.active-tab').attr('class', 'title-button');
                $(e.currentTarget).addClass('active-tab');
                $(e.currentTarget).append('<span class="tab-line"></span>');
                $introduction.show();
                $snsWrapper.show();
                $reviewWrapper.hide();
                $postsWrapper.hide();
            }
        }
        // 과외 후기 탭 누를시 이벤트
        if ($(e.currentTarget).text() === '과외 후기') {
            if (!$(e.currentTarget).attr('class').includes('active-tab')) {
                $('.tab-line').remove();
                $('.active-tab').attr('class', 'title-button');
                $(e.currentTarget).addClass('active-tab');
                $(e.currentTarget).append('<span class="tab-line"></span>');
                $introduction.hide();
                $snsWrapper.hide();
                $reviewWrapper.show();
                $postsWrapper.hide();
            }
        }
        // 과외 후기 탭 누를시 이벤트
        if ($(e.currentTarget).text() === '작성 글') {
            if (!$(e.currentTarget).attr('class').includes('active-tab')) {
                $('.tab-line').remove();
                $('.active-tab').attr('class', 'title-button');
                $(e.currentTarget).addClass('active-tab');
                $(e.currentTarget).append('<span class="tab-line"></span>');
                $introduction.hide();
                $snsWrapper.hide();
                $reviewWrapper.hide();
                $postsWrapper.show();
            }
        }
    });

    // 모달창 클릭 이벤트
    $lessonBtn.click(() => { $modal.show()});
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
