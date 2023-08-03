// $('.filter-button').on('click', () => {
//   console.log("클릭");
//   ;
// });

// $('.category-select').on('focusout', () => {
//   $('.filter-modal').css('display', 'none');
// });

function showCatagoryFilter() {
  console.log("함수");
  if ($('#modal')) {
    return;
  }
  const modal = `<div id="modal">
    <div class="category-select">
      <div class="category-wrapper">
        <h4 class="category-title">언어 설정</h4>
        <div style="height: 24px"></div>
        <div class="category-tag-container">
          <label class="category-tag">
            <input type="checkbox" class="category-input" />
            <span class="category-tag-name">한국어</span>
          </label>
          <label class="category-tag">
            <input type="checkbox" class="category-input" />
            <span class="category-tag-name">영어</span>
          </label>
          <label class="category-tag">
            <input type="checkbox" class="category-input" />
            <span class="category-tag-name">일본어</span>
          </label>
          <label class="category-tag">
            <input type="checkbox" class="category-input" />
            <span class="category-tag-name">중국어</span>
          </label>
          <label class="category-tag">
            <input type="checkbox" class="category-input" />
            <span class="category-tag-name">독일어</span>
          </label>
          <label class="category-tag">
            <input type="checkbox" class="category-input" />
            <span class="category-tag-name">스페인어</span>
          </label>
          <label class="category-tag">
            <input type="checkbox" class="category-input" />
            <span class="category-tag-name">프랑스어</span>
          </label>
          <label class="category-tag">
            <input type="checkbox" class="category-input" />
            <span class="category-tag-name">스웨덴어</span>
          </label>
          <label class="category-tag">
            <input type="checkbox" class="category-input" />
            <span class="category-tag-name">베트남어</span>
          </label>
          <label class="category-tag">
            <input type="checkbox" class="category-input" />
            <span class="category-tag-name">태국어</span>
          </label>
          <label class="category-tag">
            <input type="checkbox" class="category-input" />
            <span class="category-tag-name">그리스어</span>
          </label>
          <label class="category-tag">
            <input type="checkbox" class="category-input" />
            <span class="category-tag-name">러시아어</span>
          </label>
        </div>
        <div style="height: 24px"></div>
        <button type="button" class="category-apply">적용</button>
      </div>
    </div>
    <div class="filter-blur"></div>
  </div>`;
  $('.filter-modal').append(modal);
}

// $('body').click(function (e) {
//   if (!$('.filter-modal').find(e.target).length) {
//     $('#modal').remove();
//   }
// });
