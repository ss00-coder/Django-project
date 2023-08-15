/* tinymce */
tinymce.init({
  selector: 'textarea#image-tools',
  height: 474,
  plugins: [
    'advlist autolink lists link image charmap print preview anchor',
    'searchreplace visualblocks code fullscreen',
    'insertdatetime media table paste imagetools wordcount',
  ],
  toolbar:
    'insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
  content_style:
    'body { font-family:Helvetica,Arial,sans-serif; font-size:16px; font-weight: 400; }',
  content_style: `.mce-content-body[data-mce-placeholder]:not(.mce-visualblocks)::before {
      font-weight: 400;
      font-size: 16px;
      line-height: 16px;
      color: #c0b9bb;
      fill: #c0b9bb;
    }
    `,
  placeholder: '내용을 입력해주세요.',
});

/* 태그 추가 */
function enterkey() {
  if (window.event.keyCode == 13) {
    // 엔터키가 눌렸을 때
    text = `<li class="tag-wrapper">
              <span class="tag-text">${$("#tag-input").val()}</span>
              <button onclick="removeTag(this)" type="button">
                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                  <path
                    d="M5.707 5.707a1 1 0 0 0 0 1.414l4.95 4.95-4.95 4.95a1 1 0 1 0 1.414 1.414l4.95-4.95 4.95 4.95a1 1 0 0 0 1.414-1.414l-4.95-4.95 4.95-4.95a1 1 0 1 0-1.414-1.414l-4.95 4.95-4.95-4.95a1 1 0 0 0-1.414 0Z"
                  ></path>
                </svg>
              </button>
            </li>`;
    document.querySelector('.tag-ul').innerHTML += text;
    $("#tag-input").val("");
  }
}

function removeTag(button) {
  $(button).parent().remove();
}