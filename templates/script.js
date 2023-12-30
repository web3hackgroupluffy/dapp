
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
// main.js
document.getElementById('download-form').onsubmit = function() {
    var ipfsHash = document.getElementById('ipfs-hash').value;
    var downloadUrl = '/download-file/' + encodeURIComponent(ipfsHash);
    window.location.href = downloadUrl;
    return false; // Prevent default form submission
};

