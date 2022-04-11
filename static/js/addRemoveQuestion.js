function attachEvent() {
    const questionForm = document.querySelectorAll("form .question");
    const answerForm = document.querySelectorAll(".answer");
    const container = document.querySelector("#form-container");
    const addButton = document.getElementById("add-form");
    let formNum = questionForm.length-1;

    addButton.addEventListener('click', addQuestion);

    function addQuestion(e) {
        e.preventDefault()

        const formsetElement = document.getElementById('id_form-TOTAL_FORMS');
        let newQuestionForm = questionForm[0].cloneNode(true);
        let newAnswerForm = answerForm[0].cloneNode(true);
        let buttons = document.getElementsByClassName('buttons')[0];
        let formRegex = RegExp(`form-(\\d){1}-`,'g');

        formNum++;
        buttons.remove();
        newQuestionForm.innerHTML = newQuestionForm.innerHTML.replace(formRegex, `form-${formNum}-`);
        newAnswerForm.innerHTML = newAnswerForm.innerHTML.replace(formRegex, `form-${formNum}-`);

        if (!formsetElement) {
            newQuestionForm.children[1].name = `question${formNum}`;
            newAnswerForm.children[1].name = `answer${formNum}`;
        }

        container.insertBefore(newQuestionForm, container.children[-1]);
        container.insertBefore(newAnswerForm, container.children[-1]);
        container.insertBefore(buttons, container.children[-1]);

        let totalForms = document.querySelectorAll("#id_form-TOTAL_FORMS");
        totalForms.forEach(f => f.setAttribute('value', `${formNum+1}`));
    }

    function removeQuestion() {

    }
}