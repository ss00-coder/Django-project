/* helpers/detail.html */
$('.comment-textarea-wrapper').hide();
$('.comment-write-with-login').on('click', () => {
  $('.comment-write-with-login').hide();
  $('.comment-textarea-wrapper').show();
});
$('button.cancel-button').on('click', () => {
  $('.comment-write-with-login').show();
  $('.comment-textarea-wrapper').hide();
});

$(".heart").each((i, heart) => {
  $(heart).on('click', () => {
    $(".heart").removeClass("active");
    if(i==0){
      $(".heart").eq(1).addClass("active");
    } else {
      $(".heart").eq(0).addClass("active");
    }
  })
  
})