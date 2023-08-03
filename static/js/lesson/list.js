/* 카테고리 필터 */
$(".filter-modal").hide();

$('.filter-button').on('click', () => {
  $(".filter-modal").show();
});

$('.filter-blur').on('click', () => {
  $(".filter-modal").hide();
});