var $prev = $($(".page-button")[0]);

$(".page-button").each((i, e) => {
	var $pageNumber = $(e);

	$pageNumber.on("click", function (e) {
		e.preventDefault();
		if ($prev == $pageNumber) {
			return;
		}

		$prev.removeClass("page-button-active");
		$pageNumber.addClass("page-button-active");

		$prev = $pageNumber;
	});
});


//
// /*체크 된 게시물의 번호 가져오기*/
// const $checkBoxs = $("input[type=checkbox]");
// const $deleteButton = $(".delete-button");
//
// $deleteButton.on("click", function (e) {
// 	let boardIdArr = [];
//
// 	$checkBoxs.each((i, checkBox) => {
// 		if ($(checkBox).prop("checked")) {
// 			boardIdArr.push($(checkBox).parent().siblings(".noticeId").text());
// 		}
// 	})
// 	if (boardIdArr) {
// 		confirm(boardIdArr + "번을 삭제하시겠습니까?");
// 	} else {
// 		confirm("공지사항 게시글을 선택해주세요.");
// 	}
// 	console.log(boardIdArr);
// 	console.log(contextPath);
// 	adminNoticeService.remove(boardIdArr);
// });
//
// const adminNoticeService = (function () {
// 	function remove(boardIdArr) {
// 		$.ajax({
// 			traditional: true,
// 			url: contextPath + "/adminFreeBoardDelete.admin",
// 			data: { boardIdArr: boardIdArr },
// 			success: function () {
// 				location.reload();
// 			}
// 		});
// 	};
//
// 	return { remove: remove }
// })();