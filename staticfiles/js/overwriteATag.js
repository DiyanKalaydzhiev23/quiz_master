function changeA() {
    const a = document.querySelectorAll('#edit-profile-form a');

    if (!a) return;

    a.forEach(a => {
        if (a.textContent === "../../../media/images/default_image.png") {
            a.textContent = "Anonymous";
        }
    })
}
