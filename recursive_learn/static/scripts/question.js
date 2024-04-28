document.addEventListener('click', e => {
    const isQuestionMark = e.target.matches('[data-question-button]');

    if (!isQuestionMark && e.target.closest('[data-question]') != null) return;
    let currentQuestion ;
    if (isQuestionMark) {
        currentQuestion = e.target.closest('[data-question]');
        currentQuestion.classList.toggle('active');
    }

    document.querySelectorAll('[data-question].active').forEach(question => {
        if (question === currentQuestion) return;
        question.classList.remove('active');
    });
})