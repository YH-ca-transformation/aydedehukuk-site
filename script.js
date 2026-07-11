const yearEl = document.getElementById('year');
if (yearEl) {
  yearEl.textContent = new Date().getFullYear();
}

// Portrait image pop-up (homepage only)
const lawyerModal = document.getElementById('lawyerModal');
const lawyerModalTrigger = document.getElementById('lawyerModalTrigger');
if (lawyerModal && lawyerModalTrigger) {
  const openModal = () => {
    lawyerModal.hidden = false;
    document.body.classList.add('modal-open');
    const closeBtn = lawyerModal.querySelector('.image-modal__close');
    if (closeBtn) closeBtn.focus({ preventScroll: true });
  };
  const closeModal = () => {
    lawyerModal.hidden = true;
    document.body.classList.remove('modal-open');
    lawyerModalTrigger.focus({ preventScroll: true });
  };
  lawyerModalTrigger.addEventListener('click', (e) => {
    e.preventDefault();
    openModal();
  });
  lawyerModal.querySelectorAll('[data-modal-close]').forEach((el) => {
    el.addEventListener('click', closeModal);
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !lawyerModal.hidden) {
      closeModal();
    }
  });
}
