
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

globalThis.reviewId;

    //모달창 이벤트
    $deleteBtn.click(function(){
        globalThis.reviewId = this.id
        // console.log(this.id);
        $modal.show();
    });

    // 삭제 버튼
    $buttonCancel.click(() => { $modal.hide() })
    $buttonAgree.click(function ()  {
        console.log(reviewId)
        $modal.hide()
      if ($(".active-tab").children().children().text().trim() === "게시완료") {
            status = 'Y'
        } else if ($(".active-tab").children().children().text().trim() === "임시저장") {
            status = 'N'
        }
        location.href=`/mypage/lesson-review/delete/${globalThis.reviewId}/`
    });
});

//검색창
const $createBtn = $('.create-btn');
    $createBtn.click(() => {
        location.href=`/lesson/review/write/`
    })

$('.update-button').click(function() {
  const postId = $(this).data('post-id');
  if (postId) {
    location.href = `/lesson/review/write/${postId}`;
  }
});
// let status = 'Y';
//
// if(status_view === 'N') {
//     $(".tab-item-btn").eq(0).removeClass("active-tab");
//     $(".tab-item-btn").eq(1).addClass("active-tab");
//     $('.tab-line').remove();
//     $(".tab-item-btn").eq(1).append('<div class="tab-line"></div>');
// }

$(".search-button svg").on('click', () => {
    const keyword = $("#search-input").val();

    if (status_view === 'N') {
        window.location.href = keyword === "" ? "/mypage/lesson-review/tab/N/" : `/mypage/lesson-review/tab/N/${encodeURIComponent(keyword)}/`;
    } else {
        window.location.href = keyword === "" ? "/mypage/lesson-review/tab/Y/" : `/mypage/lesson-review/tab/Y/${encodeURIComponent(keyword)}/`;
    }
});