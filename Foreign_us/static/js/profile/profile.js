let pay_item = "untact";
let page = 1;
getList("review");
getList("lesson");

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
            page = 1;
            document.querySelector(`.add-review`).innerHTML = "";
            document.querySelector(`.add-lesson`).innerHTML = "";
        }
        // 과외 글 탭 누를시 이벤트
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
            page = 1;
            document.querySelector(`.add-review`).innerHTML = "";
            document.querySelector(`.add-lesson`).innerHTML = "";
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


// 무한스크롤
function getList(url){
    fetch(`/profile/${url}/${teacher_id}/${page}`)
        .then((response) => response.json())
        .then((posts)=>{
            let text = "";
            posts.posts.forEach(post => {
                if(url==="review"){
                    post = post[0];
                }
                text += `<div style="display: flex; align-items: flex-end; justify-content: space-between;" class="item-wrapper">
                            <div>
                                <div class="item-container">
                                    <div class="item-profile">
                                        <div class="icon-container">
                        `
                if(post.member_file){
                    text += `
                        <a href="/profile/${post.member_id}">
                            <img style="margin-top: 10px; position: relative; width: 34px; height: 34px; border-radius: 9999px"  src="/upload/${post.member_file}" alt="">
                        </a>
                    `;
                } else {
                    text += `<div style="background-image: url('/static/image/profile_icon.png')" class="item-icon"></div>`;
                }
                text +=   `      
                                        </div>
                                        <div class="info-container">
                                            <div>
                                                <a class="info-nickname" href="/profile/${post.member_id}">${post.member_nickname}</a>
                                            </div>
                                            <div class="info-flex">
                                                <a class="info-a" style="margin: 0" href="">
                                                    <span>${elapsedTime(post.created_date)}</span>
                                                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                                        <circle cx="12" cy="12" r="4"></circle>
                                                    </svg>
                                                    <span>조회수 ${post.post_view_count}</span>
                                                </a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                               `
                if(url==="review"){
                    text += `<button onclick="location.href='/lesson/review/detail/${post.id}'" class="item-text">`
                } else if (post.event_location){
                    text += `<button onclick="location.href='/event/detail/${post.id}'" class="item-text">`
                } else {
                    text += `<button onclick="location.href='/helpers/detail/${post.id}'" class="item-text">`
                }
                text += `
                                    <h4 class="item-h4">${post.post_title}</h4>
                                    <div style="height: 42px; overflow: hidden; padding-right: 5px; text-overflow: ellipsis;" class="item-content-p">
                                        ${post.post_content}
                                    </div>
                                </button>
                            </div>
                    `
                if(post.post_file){
                    text += `
                            <div class="post-image">
                                <span class="post-thumbnail">
                                  <img
                                    class="thumbnail-image"
                                    src="/upload/${post.post_file}"
                                    alt=""
                                  />
                                </span>
                            </div>
                    `
                }
                text += `    
                        </div>
                        <hr style="border: 0; height: 1px; background: #e5e7eb; margin-top: 35px;">
                    `
            })
            if(page !== 1){
                document.querySelector(`.add-${url}`).innerHTML += text;
            } else {
                document.querySelector(`.${url}-container`).innerHTML = text;
            }
        })
}

window.addEventListener('scroll', () => {
    let content = "";
    const currentScroll = window.scrollY;
    const windowHeight = window.innerHeight;
    const bodyHeight = document.body.scrollHeight;
    // console.log(currentScroll + windowHeight + 0.5, bodyHeight);
    if(currentScroll + windowHeight + 0.5 >= bodyHeight){
        if($('.title-button.active-tab').text() === "과외 후기"){
            content = "review";
        } else{
            content = "lesson";
        }
        page++;
        getList(content);
    }
});


//작성시간 함수
function elapsedTime(date) {
    const start = new Date(date);
    const end = new Date();

    const diff = (end - start) / 1000;

    const times = [
        { name: '년', milliSeconds: 60 * 60 * 24 * 365 },
        { name: '개월', milliSeconds: 60 * 60 * 24 * 30 },
        { name: '일', milliSeconds: 60 * 60 * 24 },
        { name: '시간', milliSeconds: 60 * 60 },
        { name: '분', milliSeconds: 60 },
    ];

    for (const value of times) {
        const betweenTime = Math.floor(diff / value.milliSeconds);

        if (betweenTime > 0) {
            return `${betweenTime}${value.name} 전`;
        }
    }
    return '방금 전';
}