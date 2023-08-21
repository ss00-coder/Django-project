/* 헤더 탭 */
$(".sub-header-item-content").eq(0).removeClass("sub-header-item-active");
$(".sub-header-item-content").eq(4).addClass("sub-header-item-active");


let page = 1;
// $(document).ready(getList());
getList();

function getList(){
    fetch(`/notice/list/${page}`)
        .then((response) => response.json())
        .then((posts)=>{
            console.log(posts);
            let text = "";
            posts.posts.forEach(post => {
                console.log(post);
                post = post[0];
                text += `<div>
                            <a href="/notice/detail/${post.id}">
                              <div class="recommend-one-post">
                                <button class="recommend-one-post-btn">
                                  <div class="recommend-one-post-btn-img">
                                    <span class="recommend-one-post-btn-img-span">
                                      <span></span>
                          `;
                if(post.post_file){
                    text += `<img style="object-fit: cover" src="/upload/${post.post_file}">`;
                } else {
                    text += `<img style="object-fit: cover" src="https://steadio.co/_next/image?url=https%3A%2F%2Fsteadio.imgix.net%2Fsub_banners%2F0731_%25EC%2582%25AC%25EB%259D%25BC%25EC%259E%2588%25EB%2584%25A4.png%3Fauto%3Dformat%252Ccompress%26h%3D840%26lossless%3Dtrue%26w%3D840&w=1920&q=75">`;
                }
                text += `                
                                    </span>
                                  </div>
                                  <section class="recommend-one-post-btn-content">
                                    <div>
                                      <strong class="recommend-one-post-btn-content-strong">공지사항</strong>
                                      <h2 class="recommend-one-post-btn-content-h2">${post.post_title}</h2>
                                    </div>
                                    <div style="width: 40px; height: 2px; background-color: #333334;"></div>
                                    <p style="overflow: hidden; height: 96px" class="recommend-one-post-btn-content-p">${post.post_content}</p>
                                  </section>
                                </button>
                              </div>
                            </a>
                        </div>
                    `
            })
            document.querySelector("#post-wrapper").innerHTML += text;
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