/*체크 된 게시물의 번호 가져오기*/
const $checkBoxs = $("input[type=checkbox]");
const $deleteButton = $(".delete-button");


$deleteButton.on("click", function (e) {
	let memberIdArr = [];

	$checkBoxs.each((i, checkBox) => {
		id = $(checkBox).parent().siblings(".noticeId").text()
		if ($(checkBox).prop("checked") && id!=='') {
			memberIdArr.push(id);
		}
	})
	if (memberIdArr) {
		if(confirm(memberIdArr + "번을 탈퇴 회원으로 변경하시겠습니까?")){
			adminMemberService.remove(memberIdArr);
		}
	} else {
		confirm("탈퇴시킬 회원을 선택해주세요.");
	}
});

const adminMemberService = (function () {
	function remove(memberIdArr) {
		fetch("/administrator/member/delete/", {
			method: 'post',
			headers: {'Content-Type': 'application/json; charset=utf-8'},
			body: JSON.stringify({member_ids: memberIdArr})
		}).then(()=>{
			location.reload();
		});

	}

	return { remove: remove }
})();

// 검색
$(".search-button img").on('click', ()=>{
	keyword = $(".search-box").val();
	location.href = keyword === "" ? "/administrator/member/list/" : `/administrator/member/list/${keyword}/`;
})
