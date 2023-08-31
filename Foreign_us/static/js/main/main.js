
let page = 1;

getList();
function getList(){
    fetch(`/list/${page}`)
        .then((response) => response.json())
        .then((posts)=> {
            console.log(posts);
            if (posts.posts.length !== 0) {
                console.log(posts);
                let text = "";
                posts.posts.forEach(post => {
                    console.log(post);
                    post = post[0];
                    text += ` <li class="recommend-post-item">
                    <div>
                        <button type="button" class="recommend-post-item-btn" onclick="location.href='/helpers/detail/${post.id}'">
                            <div class="recommend-post-item-flex">
                                <div class="recommend-post-item-content">
                                    <h2>${post.post_title}</h2>
                                    <p>${post.post_content}</p>
                                </div>
                                <div class="recommend-post-item-img">
                                  <span class="recommend-post-item-img-span">
                                           `;
                                if(post.post_file){
                                    text += `<img style="object-fit: cover" src="/upload/${post.post_file}">`;
                                }
                                text += `              
                                  </span>
                                </div>
                            </div>
                            <div class="recommend-post-item-flex-sub">
                                <div class="recommend-post-item-icon"></div>
                                <div class="recommend-post-item-flex-sub-flex">
                                    <span class="recommend-post-item-sub-nickname">${post.nickname}</span>
                                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                        <circle cx="12" cy="12" r="4"></circle>
                                    </svg>
                                    <span class="recommend-post-item-sub-date">${elapsedTime(post.created_date)}</span>
                                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                        <circle cx="12" cy="12" r="4"></circle>
                                    </svg>
                                    <span class="recommend-post-item-sub-count">조회수 ${post.post_view_count}</span>
                                </div>
                            </div>
                        </button>
                    </div>
                </li>
                `
                })
                document.querySelector(".recommend-post-items").innerHTML = text;
            }
        }
    )
}

// $(window).on('load', function () {
//     load('.recommend-post-item', '5');
//     $(".recommend-post-refresh-btn").on("click", function () {
//         load('.recommend-post-item', '5', '#refresh');
//     })
// });
//
// function load(post, cnt, btn) {
//     let post_list = post.id + " .recommend-post-item:not(.active)";
//     let post_length = $(post_list).length;
//     let post_total_cnt;
//     if (cnt < post_length) {
//         post_total_cnt = cnt;
//     } else {
//         post_total_cnt = post_length;
//         $('.button').hide()
//     }
//     $(post_list + ":lt(" + post_total_cnt + ")").addClass("active");
// }




//작성시간 함수
function elapsedTime(date){
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

// 더보기 클릭 이벤트
$(".recommend-post-refresh").on('click', () => {
    page++;
    if(page === 6){
        page = 1;
    }
    $(".recommend-post-refresh-text").text(`더보기 ${page}`);
    getList();
});
