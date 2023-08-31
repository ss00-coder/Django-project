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
    $(".filter-modal").hide();

    $('.filter-button').on('click', () => {
        $(".filter-modal").show();
    });

    $('.filter-blur').on('click', () => {
        $(".filter-modal").hide();
    });

    $(".category-tag").each((i, tag) => {
        $(tag).on('click', (e) => {
            // console.log($(e.target))
            tag = $(e.target).parent();
            if (tag.hasClass("active")) {
                tag.removeClass("active");
            } else {
                tag.addClass("active");
            }
        })
    })

    $('.category-apply').on('click', () => {
        let post_filters = []
        $(".filter-modal").hide();
        $(".category-tag").each((i, tag) => {
            // console.log($(tag).hasClass("active"))
            if($(tag).hasClass("active")) {
                // console.log($(tag).children(0).val());
                // $(tag).children(0).val()s
                post_filters.push($(tag).children(0).val())
                // $('.input-values').append(`<input value='${$(tag).children(0).val()}' name="post_filter" type="hidden">`);
            }
        })
        // console.log(post_filters)
        document.querySelector(".post-wrapper").innerHTML = '';
        page = 1;
        postList(post_filters)
    });

function getList(){
    fetch(`/lesson/list/${page}/${type}`)
        .then((response) => response.json())
        .then((posts)=>{
            // console.log(posts);
            let text = "";
            posts.posts.forEach(post => {
                // console.log(post);
                post = post[0];
                text += `<li class="post">
                            <div>
                              <button type="button" class="post-link" onclick="location.href='/lesson/detail/${post.id}'">
                                <div class="post-container">
                                  <div class="post-text">
                                    <h2 class="post-title">${post.post_title}</h2>
                                    <div class="post-content">${post.post_content}</div>
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

function postList(post_filters){
    // CSRF 토큰 가져오기
    let csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    // 요청 헤더에 CSRF 토큰 추가
    let headers = {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken, // 이 부분이 중요합니다
    };
    fetch(`/lesson/list/${page}`, {
            method: 'post',
            headers: headers,
            body: JSON.stringify({post_filters: post_filters})
        }).then((response) => response.json())
        .then((posts)=>{
            // console.log(posts);
            // posts.posts[0]
            // temp = JSON.parse(posts.posts[0])
            // console.log(temp)
            // filter_post = JSON.parse(posts.posts)
            let text = "";
            // console.log(posts.posts)
            posts.posts.forEach(post => {
                post1 = JSON.parse(post[0])[0]
                post_file = JSON.parse((post[1]))[0]
                member_file = JSON.parse((post[2]))[0]
                member = JSON.parse((post[3]))[0]
                // console.log(member)
                // console.log("들어옴")
                // console.log(post1)
                // console.log(post_file)
                // console.log(member_file)
                // post1 = post1[0]
                // console.log(post1[0])
                text += `<li class="post">
                            <div>
                              <button type="button" class="post-link" onclick="location.href='/lesson/detail/${post1.pk}'">
                                <div class="post-container">
                                  <div class="post-text">
                                    <h2 class="post-title">${post1.fields.post_title}</h2>
                                    <div class="post-content">${post1.fields.post_content}</div>
                                  </div>
                                  <div class="post-image">
                                    <span class="post-thumbnail">
                            `;

                                  if(post_file) {
                                     text += `<img class="thumbnail-image" src="/upload/${post_file.fields.image}">`
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
                                if(member_file) {
                                     text += `<img src="/upload/${member_file.fields.image}">`
                                  } else {
                                     text += `<img src="/upload/member/profile_icon.png">`
                                  }
                text += `                
                              </div>
                              <div class="writer-info">
                                <span class="writer-name">${member.fields.member_nickname}</span>
                                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="writer-line">
                                  <circle cx="12" cy="12" r="4"></circle>
                                </svg>
                                <span class="write-info">${elapsedTime(post1.fields.created_date)}</span>
                                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="writer-line">
                                  <circle cx="12" cy="12" r="4"></circle>
                                </svg>
                                <span class="write-info">조회수 ${post1.fields.post_view_count}</span>
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