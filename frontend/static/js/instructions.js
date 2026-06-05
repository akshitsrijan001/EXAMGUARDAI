function enterFullscreenAndStart() {

    document.documentElement.requestFullscreen()
    .then(() => {

        window.location.href = "/exam";

    })
    .catch(() => {

        alert(
            "Please allow fullscreen mode before starting the exam."
        );

    });

}

document
.getElementById("startExamBtn")
.addEventListener(
    "click",
    enterFullscreenAndStart
);