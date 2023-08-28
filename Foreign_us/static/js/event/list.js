$(".sub-header-item-content").eq(0).removeClass("sub-header-item-active");
$(".sub-header-item-content").eq(3).addClass("sub-header-item-active");


let page = 1;
// $(document).ready(getList());
getList();

function getList(){
    fetch(`/event/list/${page}`)
        .then((response) => response.json())
        .then((posts)=>{
            console.log(posts);
            let text = "";
            posts.posts.forEach(post => {
                console.log(post);
                post = post[0];
                text += `<li class="post">
                          <a href="/event/detail/${post.id}" style="text-decoration: none; color: #030303">
                            <div>
                              <button type="button" class="post-link">
                                <div class="post-container">
                                  <div class="post-text">
                                    <h2 class="post-title">${post.post_title}</h2>
                                    <p class="post-content"> ${post.post_content} </p>
                                  </div>
                                  <div class="post-image">
                                    <span class="post-thumbnail">
                                        <span></span>
                              `;
                    if(post.post_file){
                        text += `<img style="object-fit: cover" src="/upload/${post.post_file}">`;
                    } else {
                        text += `<img style="object-fit: cover" src="https://steadio.co/_next/image?url=https%3A%2F%2Fsteadio.imgix.net%2Fsub_banners%2F0731_%25EC%2582%25AC%25EB%259D%25BC%25EC%259E%2588%25EB%2584%25A4.png%3Fauto%3Dformat%252Ccompress%26h%3D840%26lossless%3Dtrue%26w%3D840&w=1920&q=75">`;
                    }
                    text += `                
                                    </span>
                                    <div></div>
                                  </div>
                                </div>
                                <div class="post-writer">
                                  <div class="writer-profile-image"></div>
                                  <div class="writer-info">
                                    <span class="writer-name" >${post.nickname ? post.nickname : '유저'}</span>
                                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="writer-line">
                                      <circle cx="12" cy="12" r="4"></circle>
                                    </svg>
                                    <span class="write-info">${elapsedTime(post.created_date)}</span>
                                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="writer-line">
                                      <circle cx="12" cy="12" r="4"></circle>
                                    </svg>
                                    <span class="write-info">${post.post_view_count}</span>
                                  </div>
                                </div>
                              </button>
                            </div>
                          </a>
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

//작성시간 함수
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