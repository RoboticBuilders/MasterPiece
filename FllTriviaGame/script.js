//References
let timeLeft = document.querySelector(".time-left");
let quizContainer = document.getElementById("container");
let nextBtn = document.getElementById("next-button");
let countOfQuestion = document.querySelector(".number-of-question");
let displayContainer = document.getElementById("display-container");
let scoreContainer = document.querySelector(".score-container");
let restart = document.getElementById("restart");
let userScore = document.getElementById("user-score");
let startScreen = document.querySelector(".start-screen");
let startButton = document.getElementById("start-button");
let name = document.getElementById("name");
let tname = document.getElementById("tname");
let tst = document.getElementById("top-score-table");
let questionCount;
let scoreCount = 0;
let count = 11;
let countdown;
let nameValue;
let tnameValue;

//Questions and Options array

const quizArray = [
    {
        id: "0",
        question: "What does FLL stand for?",
        options: ["First Lego League", "First Little League", "Front Level League", "Fellow Little League"],
        correct: "First Lego League",
    },
    {
        id: "1",
        question: "Who is the founder of FIRST?",
        options: ["Salman Khan", "Bill Gates", "Dean Kamen", "Steve Jobs"],
        correct: "Dean Kamen",
    },
    {
        id: "2",
        question: "What is the FLL Motto?",
        options: ["Great Robotics", "More Than Robots", "Robotics for everyone", "More Than Robot"],
        correct: "More Than Robots",
    },
    {
        id: "3",
        question: "What programming languages can one use to code in FLL?",
        options: ["python, word blocks", "word blocks", "javascript, word blocks", "python"],
        correct: "python, word blocks",
    },
    {
        id: "4",
        question: "When one drives a 24 tooth gear using a 8 tooth gear, what happens?",
        options: ["Increases Torque and speed", "Increases Speed, decreases torque", "Decreases Speed, increases torque", "Decreases Torque"],
        correct: "Decreases Speed, increases torque",
    },
    {
        id: "5",
        question: "A worm gear is used to?",
        options: ["Increase speed", "Increase both speed and torque", "Decrease torque and speed", "Increase torque"],
        correct: "Increase torque",
    }, {
        id: "6",
        question: "What was the 2022-2023 season called?",
        options: ["SuperPowered", "Replay", "Into Orbit", "CityShaper"],
        correct: "SuperPowered",
    },
    {
        id: "7",
        question: "How many teams participated in City Shaper?",
        options: [">80000", ">1000", ">10000", ">38000"],
        correct: ">38000",
    },
    {
        id: "8",
        question: "What was the first year of FLL?",
        options: ["2010-2011", "1999-2000", "2003-2004", "2008-2009"],
        correct: "1999-2000",
    },
    {
        id: "9",
        question: "What was the first Lego robotics kit called?",
        options: ["RIS", "RCX", "NXT", "MindStorms"],
        correct: "RCX",
    },
    {
        id: "10",
        question: "What was the first Lego robotics kit called?",
        options: ["RIS", "RCX", "NXT", "MindStorms"],
        correct: "RCX",
    },
];

//Restart Quiz
restart.addEventListener("click", () => {
    //displayContainer.classList.add("hide");
    //initial();

    //displayContainer.classList.remove("hide");
    scoreContainer.classList.add("hide");
    startScreen.classList.remove("hide");
    displayContainer.classList.add("hide");
});

//Next Button
nextBtn.addEventListener(
    "click",
    (displayNext = () => {
        //increment questionCount
        questionCount += 1;
        //if last question
        if (questionCount == quizArray.length) {
            //hide question container and display score
            displayContainer.classList.add("hide");
            scoreContainer.classList.remove("hide");
            //user score
            userScore.innerHTML =
                "Your score is " + scoreCount + " out of " + questionCount;

	    //alert(tnameValue)
	    tst.innerHTML = tst.innerHTML + "<div>" + "team name = " + tnameValue + "        name = " + nameValue + "          " + scoreCount + "</div>"
        } else {
            //display questionCount
            countOfQuestion.innerHTML =
                questionCount + 1 + " of " + quizArray.length + " Question";
            //display quiz
            quizDisplay(questionCount);
            count = 11;
            clearInterval(countdown);
            timerDisplay();
        }
    })
);

//Timer
const timerDisplay = () => {
    countdown = setInterval(() => {
        count--;
        timeLeft.innerHTML = `${count}s`;
        if (count == 0) {
            clearInterval(countdown);
            displayNext();
        }
    }, 1000);
};

//Display quiz
const quizDisplay = (questionCount) => {
    let quizCards = document.querySelectorAll(".container-mid");
    //Hide other cards
    quizCards.forEach((card) => {
        card.classList.add("hide");
    });
    //display current question card
    quizCards[questionCount].classList.remove("hide");
};

//Quiz Creation
function quizCreator() {
    //randomly sort questions
    quizArray.sort(() => Math.random() - 0.5);
    //generate quiz
    for (let i of quizArray) {
        //randomly sort options
        i.options.sort(() => Math.random() - 0.5);
        //quiz card creation
        let div = document.createElement("div");
        div.classList.add("container-mid", "hide");
        //question number
        countOfQuestion.innerHTML = 1 + " of " + quizArray.length + " Question";
        //question
        let question_DIV = document.createElement("p");
        question_DIV.classList.add("question");
        question_DIV.innerHTML = i.question;
        div.appendChild(question_DIV);
        //options
        div.innerHTML += `
    <button class="option-div" onclick="checker(this)">${i.options[0]}</button>
     <button class="option-div" onclick="checker(this)">${i.options[1]}</button>
      <button class="option-div" onclick="checker(this)">${i.options[2]}</button>
       <button class="option-div" onclick="checker(this)">${i.options[3]}</button>
    `;
        quizContainer.appendChild(div);
    }
}

//Checker Function to check if option is correct or not
function checker(userOption) {
    let userSolution = userOption.innerText;
    let question =
        document.getElementsByClassName("container-mid")[questionCount];
    let options = question.querySelectorAll(".option-div");

    //if user clicked answer == correct option stored in object
    if (userSolution === quizArray[questionCount].correct) {
        userOption.classList.add("correct");
        scoreCount++;
    } else {
        userOption.classList.add("incorrect");
        //For marking the correct option
        options.forEach((element) => {
            if (element.innerText == quizArray[questionCount].correct) {
                element.classList.add("correct");
            }
        });
    }

    //clear interval(stop timer)
    clearInterval(countdown);
    //disable all options
    options.forEach((element) => {
        element.disabled = true;
    });
}

//initial setup
function initial() {
    quizContainer.innerHTML = "";
    questionCount = 0;
    scoreCount = 0;
    count = 11;
    clearInterval(countdown);
    timerDisplay();
    quizCreator();
    quizDisplay(questionCount);
}

//when user click on start button
startButton.addEventListener("click", () => {	    
    nameValue =  name.value
    tnameValue = tname.value

    startScreen.classList.add("hide");
    displayContainer.classList.remove("hide");
    initial();
});

//hide quiz and display start screen
window.onload = () => {
    startScreen.classList.remove("hide");
    displayContainer.classList.add("hide");
};