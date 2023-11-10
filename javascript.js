document.addEventListener("DOMContentLoaded", function () {
    var audio = document.getElementById("backgroundMusic");

    if (audio) {
        audio.play();

        document.querySelectorAll("a").forEach(function (link) {
            link.addEventListener("click", function (event) {
                event.preventDefault();
                audio.pause();
                window.location.href = link.getAttribute("href");
            });
        });
    }
});
