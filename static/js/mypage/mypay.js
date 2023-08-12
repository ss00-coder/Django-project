
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


    //모달창 이벤트
    $deleteBtn.click(() => { $modal.show() });
    $buttonCancel.click(() => { $modal.hide() })
    $buttonAgree.click(() => { $modal.hide() })
});




