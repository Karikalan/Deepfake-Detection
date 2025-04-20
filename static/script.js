document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("uploadForm").addEventListener("submit", function(event) {
        event.preventDefault();
        document.getElementById("result").innerText = "Uploading...";
        setTimeout(() => {
            this.submit();
        }, 1500);
    });
});