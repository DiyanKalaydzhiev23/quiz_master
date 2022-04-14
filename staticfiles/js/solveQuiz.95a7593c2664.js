let onQuestion = 0;
let startTime;

function startQuiz() {
    const form = document.getElementById('form-container');

    if (form.style.display !== 'none') return;

    const title = document.getElementById('title');
    const totalQuestions = document.getElementById('id_total_questions');

    totalQuestions.value = document.querySelectorAll('.question input').length;
    title.textContent = document.getElementsByName('name')[0].value;
    loadNextQuestion();
}


function submitQuiz() {
    const submitBtn = document.getElementById('submitBtn');
    submitBtn.click();
}


function loadNextQuestion() {
    const questions = document.querySelectorAll('.question input');
    const currentQuestion = document.getElementById('currentQuestion');
    const answerField = document.getElementById('answerField');
    const checkBtn = document.getElementById('sendAnswerBtn');

    if (onQuestion === questions.length) {
        const resultBox = document.getElementById('resultBox');
        const averageTime = document.getElementById('id_average_time');
        const correctWrongAnswers = document.getElementById('correctWrongAnswers');
        const correctAnswersCounter = document.getElementById('id_correct_answers');
        const accuracyField = document.getElementById('accuracyField');
        const averageTimeField = document.getElementById('averageTimeField');
        const totalQuestions = document.getElementById('id_total_questions');
        const sendBtn = document.getElementById('sendBtn');

        resultBox.style.display = 'inline-block';

        correctWrongAnswers.textContent = `Answers: ${correctAnswersCounter.value} out of ${totalQuestions.value}.`;
        averageTimeField.textContent = `Average time on a quiz: ${Number(averageTime.value).toFixed(2)}s`;
        accuracyField.textContent = `Accuracy: ${(Number(correctAnswersCounter.value) / Number(totalQuestions.value)).toFixed(2) * 100}%`

        sendBtn.addEventListener('click', submitQuiz);

        return;
    }

    currentQuestion.textContent = questions[onQuestion].value;
    answerField.value = '';

    checkBtn.addEventListener('click', checkAnswers);

    startTime = new Date();
}

function checkAnswers() {
    const averageTime = document.getElementById('id_average_time');
    const checkBtn = document.getElementById('sendAnswerBtn');
    const userAnswer = document.getElementById('answerField').value;
    const realAnswer = document.querySelectorAll('.answer input')[onQuestion].value;
    const endTime = new Date();
    const timeInMilliseconds = startTime.getTime() - endTime.getTime();

    checkBtn.removeEventListener('click', checkAnswers);

    if (!averageTime.value) {
        averageTime.value = Math.abs((timeInMilliseconds) / 1000);
    } else{
         averageTime.value = Math.abs((((Number(averageTime.value) * 1000) + timeInMilliseconds) / 2) /1000);
    }

    if (userAnswer === realAnswer) {
        correctAnswer();
    } else {
        compareAnswers(userAnswer, realAnswer);
    }
}

function compareAnswers(userAnswer, realAnswer) {
    const manualCheckAnswer = document.getElementById('manualCheckAnswer');
    const yourAnswerHolder = document.getElementById('yourAnswer');
    const realAnswerHolder = document.getElementById('realAnswer');
    const sameAnswerBtn = document.getElementById('sameAnswerBtn');
    const otherAnswerBtn = document.getElementById('otherAnswerBtn');

    yourAnswerHolder.textContent = `Your answer: ${userAnswer}`;
    realAnswerHolder.textContent = `Real answer: ${realAnswer}`;

    sameAnswerBtn.addEventListener('click', correctAnswer);
    otherAnswerBtn.addEventListener('click', incorrectAnswer);

    manualCheckAnswer.style.display = 'inline-block';
}

function correctAnswer() {
    const manualCheckAnswer = document.getElementById('manualCheckAnswer');
    const correctAnswerDiv = document.getElementById('correctAnswer');
    const correctAnswersCounter = document.getElementById('id_correct_answers');

    manualCheckAnswer.style.display = 'none';
    correctAnswerDiv.style.display = 'inline-block';

    setTimeout(() => {
        correctAnswerDiv.style.display = 'none';
        correctAnswersCounter.value = Number(correctAnswersCounter.value) + 1;
        onQuestion++;
        loadNextQuestion();
    }, 2000);
}

function incorrectAnswer() {
    const manualCheckAnswer = document.getElementById('manualCheckAnswer');
    const incorrectAnswerDiv = document.getElementById('incorrectAnswer');

    manualCheckAnswer.style.display = 'none';
    incorrectAnswerDiv.style.display = 'inline-block';

    setTimeout(() => {
        incorrectAnswerDiv.style.display = 'none';
        onQuestion++;
        loadNextQuestion();
    }, 2000);
}