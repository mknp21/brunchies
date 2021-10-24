const imgDiv = $('.profile-pic-div');
const img = $('#photo');
const file = $('#file');
const uploadBtn = document.querySelector('#uploadBtn')

// if user hovers on profile div
imgDiv.on('mouseover', function() {
    uploadBtn.style.display = 'block';
});
