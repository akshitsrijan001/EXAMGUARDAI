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