function positionQuestionsAndAnswers() {
    const questions = document.querySelectorAll('form .question');
    const answers = document.querySelectorAll('.answer');
    const buttons = document.querySelector('.buttons');
    const form = document.querySelector('#form-container');
    const formsetElement = document.getElementById('id_form-TOTAL_FORMS');

    // questions.forEach(q => q.remove());
    // answers.forEach(a => a.remove());
    buttons.remove();

    for (let i = 0; i < questions.length; i++) {
        if (!formsetElement) {
            console.log(questions[i].children[1]);
            questions[i].children[1].name = `question${i}`;
            answers[i].children[1].name = `answer${i}`;
        }

        form.appendChild(questions[i]);
        form.appendChild(answers[i]);
    }

    form.appendChild(buttons);
}