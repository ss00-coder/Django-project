/*체크 된 게시물의 번호 가져오기*/
const $checkBoxs = $("input[type=checkbox]");
const $deleteButton = $(".delete-button");


$deleteButton.on("click", function (e) {
	let postIdArr = [];

	$checkBoxs.each((i, checkBox) => {
		id = $(checkBox).parent().siblings(".noticeId").text()
		if ($(checkBox).prop("checked") && id!=='') {
			postIdArr.push(id);
		}
	})
	if (postIdArr) {
		if(confirm(postIdArr + "번을 결제 취소하시겠습니까?")){
			adminLessonService.remove(postIdArr);
		}
	} else {
		confirm("과외 게시글을 선택해주세요.");
	}
});

const adminLessonService = (function () {
	function remove(postIdArr) {
		fetch("/administrator/board/lesson/delete/", {
			method: 'post',
			headers: {'Content-Type': 'application/json; charset=utf-8'},
			body: JSON.stringify({post_ids: postIdArr})
		}).then(()=>{
			location.reload();
		});

	}

	return { remove: remove }
})();

// 검색
$(".search-button img").on('click', ()=>{
	keyword = $(".search-box").val();
	location.href = keyword === "" ? "/administrator/board/lesson/list/" : `/administrator/board/lesson/list/${keyword}/`;
})
