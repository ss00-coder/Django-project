
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
    $totalNumber.text($tabBtn.eq(0).find('.tab-number').text())

    // 탭 버튼 이벤트
    $tabBtn.click((e) => {
        if (!$(e.currentTarget).attr('class').includes('active-tab')) {
            $tabBtn.toggleClass("active-tab");
            $('.tab-line').remove();
            $(e.currentTarget).append('<div class="tab-line"></div>');

            // 해당 작성글 전체 수 변경하는 이벤트
            $totalNumber.text($(e.currentTarget).find('.tab-number').text());
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
    $buttonAgree.click(function ()  {
        console.log(eventId)
        $modal.hide()
        location.href=`/mypage/event/delete/${globalThis.eventId}/`
    })
});

//검색창
$(".search-button svg").on('click', ()=>{
	keyword = $("#search-input").val();
	location.href = keyword === "" ? "/mypage/event/" : `/mypage/event/${keyword}/`;
})


