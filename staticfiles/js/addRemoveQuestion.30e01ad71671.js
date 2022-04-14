function attachEvent() {
    const questionForm = document.querySelectorAll("form .question");
    const answerForm = document.querySelectorAll(".answer");
    const container = document.querySelector("#form-container");
    const addButton = document.getElementById("add-form");
    const removeButton = document.getElementById("remove-form");

    if (removeButton) {
        addButton.addEventListener('click', addQuestion);
        removeButton.addEventListener('click', removeQuestion);
    }
    console.log(questionForm.length)
    if (questionForm.length === 1) {
        removeButton.style.display = 'none';
    }

    function addQuestion(e) {
        e.preventDefault()

        const formsetElement = document.getElementById('id_form-TOTAL_FORMS');
        let newQuestionForm = questionForm[0].cloneNode(true);
        let newAnswerForm = answerForm[0].cloneNode(true);
        let buttons = document.getElementsByClassName('buttons')[0];
        let formRegex = RegExp(`form-(\\d){1}-`,'g');
        let formNum = document.querySelectorAll("form .question").length-1;

        formNum++;
        buttons.remove();
        newQuestionForm.innerHTML = newQuestionForm.innerHTML.replace(formRegex, `form-${formNum}-`);
        newAnswerForm.innerHTML = newAnswerForm.innerHTML.replace(formRegex, `form-${formNum}-`);

        if (!formsetElement) {
            newQuestionForm.children[1].name = `question${formNum}`;
            newAnswerForm.children[1].name = `answer${formNum}`;

            newQuestionForm.children[1].value = '';
            newAnswerForm.children[1].value = '';
        }

        container.insertBefore(newQuestionForm, container.children[-1]);
        container.insertBefore(newAnswerForm, container.children[-1]);
        container.insertBefore(buttons, container.children[-1]);

        if (document.querySelectorAll("form .question").length > 1) {
            removeButton.style.display = 'inline-block';
        } else {
            removeButton.style.display = 'none';
        }

        let totalForms = document.querySelectorAll("#id_form-TOTAL_FORMS");
        totalForms.forEach(f => f.setAttribute('value', `${formNum+1}`));
    }

    function removeQuestion() {
        const questionForm = document.querySelectorAll("form .question");
        const answerForm = document.querySelectorAll(".answer");

        if (questionForm.length > 1) {
            questionForm[questionForm.length - 1].remove();
            answerForm[questionForm.length - 1].remove();
        }

        if (questionForm.length  === 1) {
            removeButton.style.display = 'none';
        }
    }
}