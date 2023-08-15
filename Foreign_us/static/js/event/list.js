/* event/list.html */

/* 정렬 필터 */
$(".order-label").each((i, order) => {
  $(order).on('click', (e) => {
    $(".order-label").removeClass("active");
    $(e.target).parent().addClass("active");
  });
});

/* 카테고리 필터 */
$(".filter-modal").hide();

$('.filter-button').on('click', () => {
  $(".filter-modal").show();
});

$('.filter-blur').on('click', () => {
  $(".filter-modal").hide();
});

$(".category-tag").each((i, tag) => {
  $(tag).on('click', (e) => {
    tag = $(e.target).parent();
    if(tag.hasClass("active")){
      tag.removeClass("active");
    } else{
      tag.addClass("active");
    }
  })
})

$('.category-apply').on('click', () => {
  $(".filter-modal").hide();
});