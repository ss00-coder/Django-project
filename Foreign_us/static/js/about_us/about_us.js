
$(function () {

     const $tabBtn = $('.title-button');
     const $tutor = $('.lesson');
     const $help_us = $('.help_us');
     const $event = $('.event');
     const $suggestion_wrap = $('.suggestion_wrap');

     // 탭 버튼 이벤트
     $tabBtn.click((e) => {

         // 과외 탭 누를시 이벤트
         if ($(e.currentTarget).text().includes('과외')) {
             if (!$(e.currentTarget).attr('class').includes('active-tab')) {
                 $('.tab-line').remove();
                 $('.active-tab').attr('class', 'title-button');
                 $(e.currentTarget).addClass('active-tab');
                 $(e.currentTarget).append('<span class="tab-line"></span>');
                 $tutor.show();
                 $help_us.hide();
                 $event.hide();
                 $suggestion_wrap.show()
             }
         }
         // 헬퍼스 탭 누를시 이벤트
         if ($(e.currentTarget).text() === '헬퍼스') {
             if (!$(e.currentTarget).attr('class').includes('active-tab')) {
                 $('.tab-line').remove();
                 $('.active-tab').attr('class', 'title-button');
                 $(e.currentTarget).addClass('active-tab');
                 $(e.currentTarget).append('<span class="tab-line"></span>');
                 $tutor.hide();
                 $help_us.show();
                 $event.hide();
                 $suggestion_wrap.show()
             }
         }
         // 이벤트 탭 누를시 이벤트
         if ($(e.currentTarget).text() === '이벤트') {
             if (!$(e.currentTarget).attr('class').includes('active-tab')) {
                 $('.tab-line').remove();
                 $('.active-tab').attr('class', 'title-button');
                 $(e.currentTarget).addClass('active-tab');
                 $(e.currentTarget).append('<span class="tab-line"></span>');
                 $tutor.hide();
                 $help_us.hide();
                 $event.show();
                 $suggestion_wrap.show()
             }
         }
     });
 });