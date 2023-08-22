function cancelPay(){
    let postIdArr = [id]
    if(confirm(postIdArr + "번을 결제 취소하시겠습니까?")){
        fetch("/administrator/board/lesson-match/delete/", {
            method: 'post',
            headers: {'Content-Type': 'application/json; charset=utf-8'},
            body: JSON.stringify({post_ids: postIdArr})
        }).then(()=>{
            location.reload();
        });
    }
}

// function checkReview(member_id, reviewed_member_id){
    // fetch(`/administrator/board/lesson-review/exist/${member_id}/${reviewed_member_id}`, {
    //     method: 'get',
    //     headers: {'Content-Type': 'application/json; charset=utf-8'},
    // }).then((response)=> response.json())
    // .then((check) => {
    //     console.log(check);
    // })
// }

// checkReview(1,2);

fetch(`/administrator/board/lesson-review/exist/${member_id}/${teacher_id}`, {
    method: 'get',
    headers: {'Content-Type': 'application/json; charset=utf-8'},
}).then((response)=> response.json())
.then((review) => {
    if(review.id){
        document.getElementById("student-review").innerHTML = `
            <button style="margin-top: 106px;" class="review-btn" type="button">
                <a href="/administrator/board/lesson-review/detail/${keyword}/${review.id}/${page}/">
                    후기
                </a>
            </button>
        `;
    }
})

fetch(`/administrator/board/lesson-review/exist/${teacher_id}/${member_id}`, {
    method: 'get',
    headers: {'Content-Type': 'application/json; charset=utf-8'},
}).then((response)=> response.json())
.then((review) => {
    if(review.id){
        document.getElementById("teacher-review").innerHTML = `
            <button style="margin-top: 106px;" class="review-btn" type="button">
                <a href="/administrator/board/lesson-review/detail/${keyword}/${review.id}/${page}/">
                    후기
                </a>
            </button>
        `;
    }
})