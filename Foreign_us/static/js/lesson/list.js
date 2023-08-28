/* lesson/list.html */

let page = 1;
let type = 'new_post'
let filter = []
// $(document).ready(getList());
getList();


/* 정렬 필터 */
$('.order-btn').click((e) => {
    if ($(e.currentTarget).text() === '인기글') {
        if(!$(e.currentTarget).hasClass('active-post')) {
            $('.order-btn').toggleClass('active-post');
            document.querySelector(".post-wrapper").innerHTML = '';
            type = 'popular_post';
            page = 1;
            getList()
        }
    }

    if ($(e.currentTarget).text() === '최신글') {
        if(!$(e.currentTarget).hasClass('active-post')) {
            $('.order-btn').toggleClass('active-post');
            document.querySelector(".post-wrapper").innerHTML = '';
            type = 'new_post';
            page = 1;
            getList()
        }
    }
})

/* 카테고리 필터 */
function loading () {
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
            if (tag.hasClass("active")) {
                tag.removeClass("active");
            } else {
                tag.addClass("active");
            }
        })
    })

    $('.category-apply').on('click', () => {
        $(".filter-modal").hide();
    });
}

function getList(){
    fetch(`/lesson/list/${page}/${type}`)
        .then((response) => response.json())
        .then((posts)=>{
            console.log(posts);
            let text = "";
            posts.posts.forEach(post => {
                console.log(post);
                post = post[0];
                text += `<li class="post">
                            <div>
                              <button type="button" class="post-link" onclick="location.href='/lesson/detail/${post.id}'">
                                <div class="post-container">
                                  <div class="post-text">
                                    <h2 class="post-title">${post.post_title}</h2>
                                    <p class="post-content">${post.post_content}</p>
                                  </div>
                                  <div class="post-image">
                                    <span class="post-thumbnail">
                            `;

                                  if(post.post_file) {
                                     text += `<img class="thumbnail-image" src="/upload/${post.post_file}">`
                                  } else {
                                     text += `<img class="thumbnail-image" src="" hidden>`
                                  }
                text += `                  
                                </span>
                                <div></div>
                              </div>
                            </div>
                            <div class="post-writer">
                              <div class="writer-profile-image">
                            `;
                                if(post.member_file) {
                                     text += `<img src="/upload/${post.member_file}">`
                                  } else {
                                     text += `<img src="/upload/member/profile_icon.png">`
                                  }
                text += `                
                              </div>
                              <div class="writer-info">
                                <span class="writer-name">${post.member__member_nickname}</span>
                                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="writer-line">
                                  <circle cx="12" cy="12" r="4"></circle>
                                </svg>
                                <span class="write-info">${elapsedTime(post.created_date)}</span>
                                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="writer-line">
                                  <circle cx="12" cy="12" r="4"></circle>
                                </svg>
                                <span class="write-info">조회수 ${post.post_view_count}</span>
                              </div>
                            </div>
                          </button>
                        </div>
                      </li>
                    `
            })
            document.querySelector(".post-wrapper").innerHTML += text;
        })
}




window.addEventListener('scroll', () => {
    const currentScroll = window.scrollY;
    const windowHeight = window.innerHeight;
    const bodyHeight = document.body.scrollHeight;
    // console.log(currentScroll + windowHeight + 20, bodyHeight);
    if(currentScroll + windowHeight + 0.5 >= bodyHeight){
        // currentScroll + windowHeight >= bodyHeight
        page++;
        getList();
    }
});

function elapsedTime(date) {
    const start = new Date(date);
    const end = new Date();

    const diff = (end - start) / 1000;

    const times = [
        { name: '년', milliSeconds: 60 * 60 * 24 * 365 },
        { name: '개월', milliSeconds: 60 * 60 * 24 * 30 },
        { name: '일', milliSeconds: 60 * 60 * 24 },
        { name: '시간', milliSeconds: 60 * 60 },
        { name: '분', milliSeconds: 60 },
    ];

    for (const value of times) {
        const betweenTime = Math.floor(diff / value.milliSeconds);

        if (betweenTime > 0) {
            return `${betweenTime}${value.name} 전`;
        }
    }
    return '방금 전';
}