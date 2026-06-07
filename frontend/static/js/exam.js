const webcam = document.getElementById("webcam");

// Backend handles camera
 function startCamera() {
      console.log("Backend face detection active");
}

startCamera();

    


// TIMER
let violations = 0;
let minutes = 60;
let seconds = 0;

const timer = document.getElementById("timer");

setInterval(() => {

    if(seconds === 0){

        if(minutes === 0){
            alert("Time Up!");
            submitExam();
            return;
        }

        minutes--;
        seconds = 59;

    }else{
        seconds--;
    }

    timer.innerHTML =
    `${String(minutes).padStart(2,'0')}:${String(seconds).padStart(2,'0')}`;

},1000);




// QUESTIONS

const questions = [

{
    question:"Which protocol provides reliable transport in TCP/IP?",
    options:["TCP","UDP","ICMP","ARP"]
},

{
    question:"Which layer is responsible for routing?",
    options:["Transport","Network","Session","Presentation"]
},

{
    question:"What does DNS translate?",
    options:["IP to MAC","Domain to IP","Port to IP","MAC to IP"]
},

{
    question:"Which protocol is connectionless?",
    options:["TCP","FTP","UDP","SMTP"]
},

{
    question:"Which device operates at Layer 2?",
    options:["Router","Switch","Firewall","Gateway"]
},

{
    question:"What is HTTP used for?",
    options:["Web communication","Email","Routing","Encryption"]
},

{
    question:"Which protocol sends email?",
    options:["SMTP","FTP","ARP","DNS"]
},

{
    question:"What is the default port of HTTPS?",
    options:["21","25","80","443"]
},

{
    question:"Which algorithm finds shortest path?",
    options:["Prim","Kruskal","Dijkstra","DFS"]
},

{
    question:"The monomer (X) involved in the synthesis of Nylon 6,6 gives positive carbylamine test. If 10 moles of X are analyzed using Dumas method, the amount (in grams) of nitrogen gas evolved is___;Use: Atomic mass of N (in amu) = 14",
    options:[
        "275",
        "278",
        "280",
        "282"
    ]
}

];


// VARIABLES

let currentQuestion = 0;

const answers = new Array(10).fill(null);

const reviewed = new Array(10).fill(false);

const visited = new Array(10).fill(false);

visited[0] = true;


// ELEMENTS

const questionText =
document.getElementById("questionText");

const questionNumber =
document.getElementById("questionNumber");

const optionsContainer =
document.getElementById("optionsContainer");

const progressFill =
document.querySelector(".progress-fill");

const progressText =
document.getElementById("progressText");

const nextBtn =
document.getElementById("nextBtn");

const prevBtn =
document.getElementById("prevBtn");

const reviewBtn =
document.getElementById("reviewBtn");

const paletteButtons =
document.querySelectorAll(".q-btn");

const submitBtn =
document.getElementById("submitBtn");


// LOAD QUESTION

function loadQuestion(){

    questionNumber.innerHTML =
    `Question ${currentQuestion + 1} of 10`;

    questionText.innerHTML =
    questions[currentQuestion].question;

    optionsContainer.innerHTML = "";

    questions[currentQuestion].options.forEach((option,index)=>{

        const label =
        document.createElement("label");

        label.className = "option";

        label.innerHTML = `
        <input
        type="radio"
        name="answer"
        value="${index}"
        ${answers[currentQuestion] == index ? "checked" : ""}
        >
        ${option}
        `;

        optionsContainer.appendChild(label);

    });

    updatePalette();

    updateProgress();
}


// SAVE ANSWER

document.addEventListener("change",(e)=>{

    if(e.target.name==="answer"){

        answers[currentQuestion] =
        parseInt(e.target.value);

        reviewed[currentQuestion] = false;

        updatePalette();
    }

});


// NEXT

nextBtn.addEventListener("click",()=>{

    if(currentQuestion < questions.length-1){

        currentQuestion++;

        visited[currentQuestion] = true;

        loadQuestion();
    }

});


// PREVIOUS

prevBtn.addEventListener("click",()=>{

    if(currentQuestion > 0){

        currentQuestion--;

        loadQuestion();
    }

});


// MARK REVIEW

reviewBtn.addEventListener("click",()=>{

    reviewed[currentQuestion] = true;

    updatePalette();

    alert(
    `Question ${currentQuestion+1} marked for review`
    );

});


// PALETTE COLORS

function updatePalette(){

    paletteButtons.forEach((btn,index)=>{

        btn.style.background = "#ffffff";
        btn.style.color = "#000000";

        if(visited[index]){

            btn.style.background = "#ef4444";
            btn.style.color = "#ffffff";
        }

        if(answers[index] !== null){

            btn.style.background = "#22c55e";
            btn.style.color = "#ffffff";
        }

        if(reviewed[index]){

            btn.style.background = "#f59e0b";
            btn.style.color = "#ffffff";
        }

        if(index === currentQuestion){

            btn.style.outline =
            "3px solid #60a5fa";
        }
        else{

            btn.style.outline = "none";
        }

    });

}


// PROGRESS

function updateProgress(){

    let answeredCount = 0;

    answers.forEach(ans=>{

        if(ans !== null){

            answeredCount++;
        }

    });

    const percent =
    (answeredCount / questions.length) * 100;

    progressFill.style.width =
    `${percent}%`;

    progressText.innerHTML =
    `${Math.round(percent)}% Completed`;
}


// PALETTE CLICK

paletteButtons.forEach((btn,index)=>{

    btn.addEventListener("click",()=>{

        currentQuestion = index;

        visited[index] = true;

        loadQuestion();

    });

});


// SUBMIT

submitBtn.addEventListener("click",()=>{

    let answeredCount = 0;

    answers.forEach(ans=>{

        if(ans !== null){

            answeredCount++;
        }

    });

    const confirmSubmit =
    confirm(
    `You have answered ${answeredCount} out of 10 questions.\n\nSubmit Exam?`
    );

    if(confirmSubmit){

        alert("Exam Submitted Successfully!");

        window.location.href = "/result";
    }

});


// INITIAL LOAD

loadQuestion();
document.addEventListener("visibilitychange", () => {

    if(document.hidden){

       violations = violations + 1;

document.getElementById(
    "violationCount"
).innerText =
    "Violations : " + violations;

        alert(
            "Warning!\nTab Switching Detected.\nViolation Count: "
            + violations
        );
    }

});


// -----------------------------
// FULLSCREEN BUTTON SUPPORT
// -----------------------------

function enterFullscreen() {

    if (!document.fullscreenElement) {

        document.documentElement
            .requestFullscreen()
            .catch(err => {
                console.log(err);
            });

    }
}

// -----------------------------
// AUTO SUBMIT ON TIMER END
// -----------------------------

function submitExam() {

    let answeredCount = 0;

    answers.forEach(ans => {

        if(ans !== null){
            answeredCount++;
        }

    });

    alert(
        `Exam Submitted\n\nAnswered ${answeredCount} out of ${questions.length} questions`
    );

    window.location.href = "/result";
}

// -----------------------------
// FULLSCREEN EXIT DETECTION
// -----------------------------

document.addEventListener("fullscreenchange", () => {

    if (!document.fullscreenElement) {

        violations = violations + 1;

        document.getElementById(
            "violationCount"
        ).innerText =
            "Violations : " + violations;

        alert(
            "Warning!\nFullscreen Exit Detected.\nViolation Count: "
            + violations
        );

    }

});
async function updateMonitorData() {

    try {

        const response =
            await fetch("/monitor");

        const data =
            await response.json();

        document.getElementById(
            "faceCount"
        ).innerText =
            "Faces Detected : " + data.faces;

        document.getElementById(
            "violationCount"
        ).innerText =
            "Violations : " + data.violations;
            violations = data.violations;

        if (data.faces === 0) {
            console.log("No Face Detected");
}

if (data.violations >= 25) {

    alert(
        "Maximum violations exceeded.\nExam will be submitted automatically."
    );

    window.location.href = "/result";
}


    }

    catch(error){

        console.log(
            "Monitor fetch failed",
            error
        );

    }

}

setInterval(
    updateMonitorData,
    1000
);

updateMonitorData();