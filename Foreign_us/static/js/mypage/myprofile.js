function setprofile(event) {
    var reader = new FileReader();

    reader.onload = function (event) {
        $('.profile-img').attr('src', event.target.result);
    }
    reader.readAsDataURL(event.target.files[0]);
}