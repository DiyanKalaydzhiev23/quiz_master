function attachEvent() {
    const questionForm = document.querySelectorAll(".question");
    const answerForm = document.querySelectorAll(".answer");
    const container = document.querySelector("#form-container");
    const addButton = document.getElementById("add-form");
    let totalForms = document.querySelectorAll("#id_form-TOTAL_FORMS");
    let formNum = questionForm.length-1;

    addButton.addEventListener('click', addQuestion);

    function addQuestion(e) {
        e.preventDefault()

        let newQuestionForm = questionForm[0].cloneNode(true);
        let newAnswerForm = answerForm[0].cloneNode(true);
        let formRegex = RegExp(`form-(\\d){1}-`,'g');

        formNum++;
        newQuestionForm.innerHTML = newQuestionForm.innerHTML.replace(formRegex, `form-${formNum}-`);
        newAnswerForm.innerHTML = newAnswerForm.innerHTML.replace(formRegex, `form-${formNum}-`);
        container.insertBefore(newQuestionForm, addButton);
        container.insertBefore(newAnswerForm, addButton);

        totalForms.forEach(f => f.setAttribute('value', `${formNum+1}`));
    }
}

window.onload = attachEvent;