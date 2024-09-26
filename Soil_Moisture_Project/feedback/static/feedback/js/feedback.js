const feedbackopenButton = document.getElementById('feedbackbutton');
const feedbackcloseButton = document.getElementById('feedback-close');
const feedbackModal = document.getElementById('feedbackModal');
const feedbackSubmitButton = document.getElementById('submitfeedback');
const feedbackInput = document.getElementById('feedback-input');
const feedbackTypeSelect = document.getElementById('feedbackType');

feedbackopenButton.addEventListener('click', () => {
  feedbackModal.classList.toggle('feedbackmodalon');
}
);

feedbackcloseButton.addEventListener('click', () => {
  feedbackModal.classList.toggle('feedbackmodalon');
}
);

function toggleFeedbackModal() {
  feedbackModal.classList.toggle('feedbackmodalon');
}

async function sendFeedback() {
  const csrfTokenCookie = document.cookie.split('; ').find(row => row.startsWith('csrftoken='));
  axios.defaults.headers.common['X-CSRFToken'] = csrfTokenCookie.split('=')[1];
  axios.post('/feedback/feedback/', {
    feedback: feedbackInput.value,
    feedbackType: feedbackTypeSelect.value,
  })
    .then((response) => {
      console.log(response);
      feedbackInput.value = '';
      Swal.fire({
        title: "Thank you!",
        text: "Your feedback has been submitted.",
        icon: "success"
      });
      toggleFeedbackModal();
    })
    .catch((error) => {
      console.log(error);
    });
}


feedbackSubmitButton.addEventListener('click', (e) => {
  e.preventDefault();
  sendFeedback();
})
