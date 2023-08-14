// 개인/단체 챌린지 전환 버튼
let $selectType = $($('.selection_label')[0]);
let $select_button = $('.selection_button');
$selectType.on("click", (e) => {
    console.log("버튼 누름");
    var $target = $(e.currentTarget);
    var $selected = $('div.selection.selected');
    var $hiddened = $('div.selection.is-hidden');
    $selected.removeClass('selected').addClass('is-hidden');
    $hiddened.removeClass('is-hidden').addClass('selected');
    if( $('div.select_date_wrapper').hasClass('is-hidden')){
        $('div.select_date_wrapper').removeClass('is-hidden');
    }else {
        $('div.select_date_wrapper').addClass('is-hidden');
    }
    if ($('div.selection.selected').attr('name')=='personal') {
        $('div.selection.selected').attr('name', 'group');
        $select_button.attr('value', $('div.selection.selected').attr('name'));
    } else {
        $('div.selection.selected').attr('name', 'personal');
        $select_button.attr('value', $('div.selection.selected').attr('name'));
    }
});