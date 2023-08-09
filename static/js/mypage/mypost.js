const $post_btn = $(".mypost-grid-top-posts-item-btn");
const $helpers = $(".mypost-grid-top-posts-item-helpers");
const $event = $(".mypost-grid-top-posts-item-event");
const $upload = $(".mypost-grid-top-posts-select-upload-btn");
const $upload_txt = $(".mypost-grid-top-posts-select-upload-set");
const $setbox = $(".mypost-grid-top-posts-select-upload-set-box");
const $option = $(".mypost-upload-set-box");
const $svg = $(".mypost-grid-top-posts-select-upload-svg");
const $all_count = $(".mypost-grid-top-posts-select-count");
const $list_count = $(".mypost-grid-top-posts-count-p");
const $delete = $(".mypost-grid-item-edit-delete-btn");
const $modal = $(".mypost-modal");
const $cancel = $(".mypost-modal-no");
const $agree = $(".mypost-modal-yes");
const $post_list = $(".mypost-grid-items");

$post_btn.on("click", function () {
  if (!$(this).attr("class").includes("set-text")) {
    $post_btn.toggleClass("set-text");
    $helpers.toggle();
    $event.toggle();
    $post_list.toggle();
    $.each($list_count, (i, list) => {
      if (
        $(list.parentElement.parentElement.parentElement)
          .attr("class")
          .includes("set-text")
      ) {
        $all_count.text($(list).text());
      }
    });
  }
});

$option.click((e) => {
  $(".mypost-grid-top-posts-select-upload-set").text($(e.target).text());
});

$cancel.click(() => {
  $modal.hide();
});
$agree.click(() => {
  $modal.hide();
});

$(document).click((e) => {
  if (
    $(e.target).is($upload) ||
    $(e.target).is($upload_txt) ||
    $(e.target).is($svg)
  ) {
    $upload.css("border-color", "#5b44ea");
    $setbox.show();
    $svg.html(
      "<path fill-rule='evenodd' clip-rule='evenodd' d='M20.73 15.58a1.076 1.076 0 0 1-1.587.13L12 9.168 4.857 15.71a1.076 1.076 0 0 1-1.586-.13 1.26 1.26 0 0 1 .122-1.695L12 6l8.607 7.885a1.26 1.26 0 0 1 .122 1.695Z'> </path>"
    );
  } else {
    $upload.css("border-color", "rgba(0, 0, 0, .1)");
    $setbox.hide();
    $svg.html(
      "<path fill-rule='evenodd' clip-rule='evenodd'd='M3.27 8.42a1.076 1.076 0 0 1 1.587-.13L12 14.832l7.143-6.544a1.076 1.076 0 0 1 1.586.13 1.26 1.26 0 0 1-.122 1.696L12 18l-8.607-7.885A1.26 1.26 0 0 1 3.27 8.42Z'></path>"
    );
  }

  if (
    $(e.target).is($delete) ||
    $(e.target).is(".mypost-grid-item-edit-delete-btn>svg")
  ) {
    $modal.show();
  }
});
