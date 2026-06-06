function updateClock(){

    const now = new Date();

    document.getElementById("clock").innerHTML =
    now.toLocaleTimeString();

}

setInterval(updateClock,1000);

updateClock();

const text =
"Next Generation AI Proctoring Platform";

let index = 0;

function typeEffect(){

    if(index < text.length){

        document.getElementById("typing").innerHTML +=
        text.charAt(index);

        index++;

        setTimeout(typeEffect,50);
    }

}

typeEffect();


// LOGIN + FACE VERIFICATION

document.querySelector("form").addEventListener("submit", async (e) => {

    e.preventDefault();

    const loginBtn =
    document.querySelector("button[type='submit']");

    loginBtn.innerHTML =
    "Verifying Face...";

    loginBtn.disabled = true;

    try{

        const response =
        await fetch("/verify");

        const data =
        await response.json();

        if(data.status === "success"){

            alert(
                "Candidate Verified Successfully!"
            );

            window.location.href =
            "/instructions";

        }else{

            alert(
                "Face Verification Failed!\nAccess Denied."
            );

            loginBtn.innerHTML =
            "Login";

            loginBtn.disabled = false;
        }

    }

    catch(error){

        console.log(error);

        alert(
            "Verification Server Error"
        );

        loginBtn.innerHTML =
        "Login";

        loginBtn.disabled = false;
    }

});