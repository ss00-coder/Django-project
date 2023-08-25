
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

            // 해당 작성글 전체 수 변경하는 이벤트// 삭제 버튼
            // $totalNumber.text($(e.currentTarget).find('.tab-number').text());
        }
    })

    globalThis.eventId;

    //모달창 이벤트
    $deleteBtn.click(function(){
        globalThis.eventId = this.id
        // console.log(this.id);
        $modal.show();
    });


    $buttonCancel.click(() => { $modal.hide() })
    // $buttonAgree.click(function ()  {
    //     console.log(eventId)
    //     $modal.hide()
    //     location.href=`/mypage/event/delete/${globalThis.eventId}/`
    // })
    $buttonAgree.click(function ()  {
    console.log(eventId);
    $modal.hide();
    // 현재 선택된 탭의 상태에 따라 다른 경로로 이동

        if ($(".active-tab").children().children().text().trim() === "게시완료") {
            status = 'Y'
        } else if ($(".active-tab").children().children().text().trim() === "임시저장") {
            status = 'N'
        }
        location.href=`/mypage/event/delete/${globalThis.eventId}/`
    });
});


// 작성 페이지로 이동
const $createBtn = $('.create-btn');
$createBtn.click(() => {
    location.href=`/event/write/`
})





let status = 'Y';
// $(".tab-item-btn").each((i, tab)=>{
//     $(tab).on('click', ()=>{
//         status = i === 0 ? 'Y' : 'N';
//         location.href = `/mypage/event/tab/${status}`;
//     })
// })

if(status_view === 'N'){
    $(".tab-item-btn").eq(0).removeClass("active-tab");
    $(".tab-item-btn").eq(1).addClass("active-tab");
    $('.tab-line').remove();
    $(".tab-item-btn").eq(1).append('<div class="tab-line"></div>');
}
//검색창
$(".search-button svg").on('click', () => {
    const keyword = $("#search-input").val();

    if (status_view === 'N') {
        window.location.href = keyword === "" ? "/mypage/event/tab/N/" : `/mypage/event/tab/N/${encodeURIComponent(keyword)}/`;
    } else {
        window.location.href = keyword === "" ? "/mypage/event/tab/Y/" : `/mypage/event/tab/Y/${encodeURIComponent(keyword)}/`;
    }
});

