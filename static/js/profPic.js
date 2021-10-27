const imgDiv = document.querySelector('.profile-pic-div');
const img = document.querySelector('#photo');
const file = document.querySelector('#file');
const uploadBtn = document.querySelector('#uploadBtn')

// if user hovers on prof div
imgDiv.addEventListener('mouseover', function() {
    uploadBtn.style.display = 'block';
});

// if user hovers away from prof div
imgDiv.addEventListener('mouseleave', function() {
    uploadBtn.style.display = 'none';
});

file.addEventListener('change', function() {
    // this. notation refers to the file variable
    const chosenFile = this.files[0];

    if (chosenFile) {
        const reader = new FileReader();

        reader.addEventListener('load', function() {
            img.setAttribute('src', reader.result);
        });

        reader.readAsDataURL(chosenFile);
    }
});