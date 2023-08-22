const $url = $(location).attr('href');
const $side_home = $(".side-home");
const $side_lesson = $(".side-lesson");
const $side_helpers = $(".side-helpers");
const $side_event = $(".side-event");
const $side_notice = $(".side-notice");

if ($url.match("lesson")) {
    $side_lesson.addClass('sub-header-item-active');
} else if ($url.match("helpers")) {
    $side_helpers.addClass('sub-header-item-active');
} else if ($url.match("event")) {
    $side_event.addClass('sub-header-item-active');
} else if ($url.match("notice")) {
    $side_notice.addClass('sub-header-item-active');
} else {
    $side_home.addClass('sub-header-item-active');
}


