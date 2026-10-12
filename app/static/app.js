document.addEventListener('click', (event) => {
  const dismiss = event.target.closest('[data-dismiss-message]');
  if (dismiss) dismiss.closest('.message').remove();
});
