
let dropZone = document.getElementById('drop-zone');
let fileInput = document.getElementById('file-input');

dropZone.addEventListener('dragover', function(e) {
    e.preventDefault();
    e.stopPropagation();
    dropZone.classList.add('drop-zone-hover');
});

dropZone.addEventListener('dragleave', function(e) {
    e.preventDefault();
    e.stopPropagation();
    dropZone.classList.remove('drop-zone-hover');
});

dropZone.addEventListener('drop', function(e) {
    e.preventDefault();
    e.stopPropagation();
    dropZone.classList.remove('drop-zone-hover');
    let files = e.dataTransfer.files;
    handleFiles(files);
});

fileInput.addEventListener('change', function() {
    handleFiles(fileInput.files);
});

function handleFiles(files) {
    // Process the files here
    console.log(files);
}

