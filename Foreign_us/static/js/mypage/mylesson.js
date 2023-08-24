
// 페이지 로드완료
$(function () {
    // 객체들
    const $tabBtn = $('.tab-item-btn');
    const $totalNumber = $('.total-number');
    const $deleteBtn = $('.delete-button');
    const $modal = $('.modal');
    const $buttonCancel = $('.button-cancel');
    const $buttonAgree = $('.button-agree');

    // 해당 작성글 전체 수 최초 값 설정
    // $totalNumber.text($tabBtn.eq(0).find('.tab-number').text())

    // 탭 버튼 이벤트
    $tabBtn.click((e) => {
        if (!$(e.currentTarget).attr('class').includes('active-tab')) {
            $tabBtn.toggleClass("active-tab");
            $('.tab-line').remove();
            $(e.currentTarget).append('<div class="tab-line"></div>');

            // 해당 작성글 전체 수 변경하는 이벤트
            // $totalNumber.text($(e.currentTarget).find('.tab-number').text());
        }
    })

globalThis.lessonId;

    //모달창 이벤트
    $deleteBtn.click(function(){
        globalThis.lessonId = this.id
        // console.log(this.id);
        $modal.show();
    });

    // 삭제 버튼
    $buttonCancel.click(() => { $modal.hide() })
    $buttonAgree.click(function ()  {
        console.log(lessonId)
        $modal.hide()
        location.href=`/mypage/lesson/delete/${globalThis.lessonId}/`
    })
});

const $createBtn = $('.create-btn');


$createBtn.click(() => {

    location.href=`/lesson/write/`
})
let status = 'Y';

if(status_view === 'N') {

    $(".tab-item-btn").eq(0).removeClass("active-tab");
    $(".tab-item-btn").eq(1).addClass("active-tab");
    $('.tab-line').remove();
    $(".tab-item-btn").eq(1).append('<div class="tab-line"></div>');
}




//검색창
$(".search-button svg").on('click', () => {
    const keyword = $("#search-input").val();

    if (status_view === 'N') {
        window.location.href = keyword === "" ? "/mypage/lesson/tab/N/" : `/mypage/lesson/tab/N/${encodeURIComponent(keyword)}/`;
    } else {
        window.location.href = keyword === "" ? "/mypage/lesson/tab/Y/" : `/mypage/lesson/tab/Y/${encodeURIComponent(keyword)}/`;
    }
});


