/* 헤더 탭 */
$(".sub-header-item-content").eq(0).removeClass("sub-header-item-active");
$(".sub-header-item-content").eq(4).addClass("sub-header-item-active");


/* lesson/detail.html */
$('.comment-textarea-wrapper').hide();
$('.comment-write-with-login').on('click', () => {
  $('.comment-write-with-login').hide();
  $('.comment-textarea-wrapper').show();
});
$('button.cancel-button').on('click', () => {
  $('.comment-write-with-login').show();
  $('.comment-textarea-wrapper').hide();
});

/* 댓글 */
let page = 1;
const replyService = (function(){
    async function getList(){
        const response = await fetch(`/notice/replies/list/${post_id}/${page}`);
        const replies = await response.json()
        return replies;
    }

    async function write(reply_content){
        const response = await fetch("/notice/replies/write/", {
            method: 'post',
            headers: {'Content-Type': 'application/json; charset=utf-8'},
            body: JSON.stringify({post_id: post_id, reply_content: reply_content})
        });
        // response.catch((error) => {})
    }

    async function modify(id, reply_content){
        const response = await fetch("/notice/replies/modify/", {
            method: 'post',
            headers: {'Content-Type': 'application/json; charset=utf-8'},
            body: JSON.stringify({id: id, reply_content: reply_content})
        });
        // response.catch((error) => {})
    }

    async function remove(id){
        const response = await fetch(`/notice/replies/delete/${id}`, {
            method: 'get',
            headers: {'Content-Type': 'application/json; charset=utf-8'},
        });
        // response.catch((error) => {})
    }

    return {getList: getList, write: write, modify: modify, remove: remove};
})()


const view = (function(){
    function showList(replies){
        if(replies.replies.length !== 0){
            $(".comment-title span").text(replies.total);
            $(".reply-num").text(replies.total);
            let text = "";
            replies.replies.forEach((reply) => {
                text += `
                    <li class="comment-wrapper">
                        <div class="original-reply">
                            <div class="comment">
                              <div class="comment-profile">
                                <div>
                                  <button class="comment-profile-button">
                                    <span class="profile-icon">
                                      <img
                                        src="https://steadio.co/_next/image?url=https%3A%2F%2Fsteadio.imgix.net%2Fprofiles%2F72ea0630-d1aa-4f02-bb0a-f07638e0ff92%2FprofileImage%2Fc0a7c669-e0e8-410c-b738-2caad9a51e76.jpg%3Fauto%3Dformat%252Ccompress%26h%3D300%26lossless%3Dtrue%26w%3D300&w=3840&q=75"
                                        alt=""
                                      />
                                    </span>
                                    <span></span>
                                  </button>
                                </div>
                              </div>
                              <div class="comment-content">
                                <div class="comment-writer">
                                  <div class="comment-writer-name">${reply.member_nickname}</div>
                                </div>
                                <div style="height: 5px"></div>
                                <div class="comment-text">
                                  <p><span>${reply.reply_content}</span></p>
                                </div>
                                <div style="height: 8px"></div>
                                <div class="comment-info">
                                  <div class="comment-time">
                                    <span class="time-text">${elapsedTime(reply.created_date)}</span>
                                  </div>
                            `;
                if(reply.member_nickname === member){
                   text += `      
                          <div>
                              <button onclick="modifyForm(this)" class="recomment-button" type="button">수정</button>
                              <button onclick="deleteReply(this)" class="recomment-button" type="button">삭제</button>
                              <input value="${reply.id}" type="hidden">
                          </div>
                    `;
                }
                text +=
                        `
                                </div>
                              </div>
                            </div>
                        </div>
                        <div style="display: none" class="modify-form">
                              <div style="padding: 0;" class="comment-textarea-wrapper">
                                <div class="comment-textarea-profile-wrapper">
                                  <button class="comment-textarea-profile" type="button">
                                    <span class="icon-container">
                                      <img
                                        src="https://steadio.co/_next/image?url=https%3A%2F%2Fsteadio.imgix.net%2Fprofiles%2F72ea0630-d1aa-4f02-bb0a-f07638e0ff92%2FprofileImage%2Fc0a7c669-e0e8-410c-b738-2caad9a51e76.jpg%3Fauto%3Dformat%252Ccompress%26h%3D300%26lossless%3Dtrue%26w%3D300&w=3840&q=75"
                                        alt=""
                                      />
                                    </span>
                                  </button>
                                  <div class="comment-textarea-name">
                                    <div class="name">${member}</div>
                                  </div>
                                </div>
                                <div style="height: 12px"></div>
                                <div class="comment-textarea-container">
                                  <label class="comment-textarea-label" for="comment-content">
                                    <textarea id="modify-content" placeholder="댓글을 작성해주세요...">${reply.reply_content}</textarea>
                                  </label>
                                </div>
                                <div style="height: 18px"></div>
                                <div class="comment-textarea-button-wrapper">
                                  <button onclick="modifyCancel(this)" class="cancel-button" type="button">취소</button>
                                  <button onclick="modifyReply(this)" class="write-button" type="button">수정</button>
                                  <input value="${reply.id}" type="hidden">
                                </div>
                              </div>
                          </div>
                      </li>
                `;
            });

            document.getElementById("reply").innerHTML += text;
            if (!replies.hasNext){
                $(".more-button").hide();
            }
        }

    }

    return {showList: showList};
})()


replyService.getList().then(view.showList);
getLikeCount();
checkLike();

$(".write-button").on("click", () => {
    const reply_content = document.getElementById("comment-content").value;
    replyService.write(reply_content).then(() => {
        page = 1;
        document.getElementById("reply").innerHTML = "";
        $('.comment-write-with-login').show();
        $('.comment-textarea-wrapper').hide();
        document.getElementById("comment-content").value = "";
        replyService.getList().then(view.showList);
    });

})

// 댓글 더보기 버튼
$(".more-button").on('click', ()=>{
    page++;
    replyService.getList().then(view.showList);
})

// 댓글 수정
function modifyForm(button){
    console.log(button);
    // $(".modify-form").css('display', 'block');
    // $(".original-reply").css('display', 'none');
    $(button).parents(".original-reply").next().css('display', 'block');
    $(button).parents(".original-reply").css('display', 'none');
}

function modifyCancel(button){
    $(button).parents(".modify-form").css('display', 'none');
    $(button).parents(".modify-form").prev().css('display', 'block');
}

function modifyReply(button){
    let id = $(button).next().val();
    let reply_content = document.getElementById("modify-content").value;
    replyService.modify(id, reply_content).then(()=>{
        $(button).parents(".modify-form").css('display', 'none');
        $(button).parents(".modify-form").prev().css('display', 'block');
        page = 1;
        document.getElementById("reply").innerHTML = "";
        replyService.getList().then(view.showList);
    });
}

// 댓글 삭제
function deleteReply(button){
    let id = $(button).next().val();
    replyService.remove(id);
    location.reload();
}

// 좋아요 추가
// 좋아요 삭제
$(".heart").each((i, heart) => {
  $(heart).on('click', () => {
    if(!member){return;}
    $(".heart").removeClass("active");
    if(i===0){
      $(".heart").eq(1).addClass("active");
      fetch("/notice/likes/add/", {
            method: 'post',
            headers: {'Content-Type': 'application/json; charset=utf-8'},
            body: JSON.stringify({id: post_id})
      }).then(()=>getLikeCount())
    } else {
      $(".heart").eq(0).addClass("active");
      fetch("/notice/likes/delete/", {
            method: 'post',
            headers: {'Content-Type': 'application/json; charset=utf-8'},
            body: JSON.stringify({id: post_id})
      }).then(()=>getLikeCount())
    }
  })
})
// 좋아요 갯수
function getLikeCount(){
    let id = post_id;
    fetch(`/notice/likes/count/${id}`, {
            method: 'get',
            headers: {'Content-Type': 'application/json; charset=utf-8'},
    }).then((response) => response.json())
    .then((count)=>{
        $(".like-num").text(count);
    })
}

//좋아요 유무
function checkLike(){
    if(!member){
        return;
    }
    fetch(`/notice/likes/exist/${post_id}`, {
        method: 'get',
        headers: {'Content-Type': 'application/json; charset=utf-8'},
    }).then((response)=> response.json())
        .then((check) => {
            $(".heart").removeClass("active");
            if(check){
                $(".heart").eq(1).addClass("active");
            }else{
                $(".heart").eq(0).addClass("active");
            }
        })
}


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