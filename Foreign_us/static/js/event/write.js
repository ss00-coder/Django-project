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
