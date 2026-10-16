// Faili eesmärk: sulgeda kasutaja nupuvajutuse peale lehel kuvatav tagasisideteade.

// Üks dokumendi klõpsukuulaja teenindab kõiki teate sulgemise nuppe.
document.addEventListener('click', (event) => {
  // closest leiab nupu ka siis, kui klõps tabab selle sees olevat elementi.
  const dismiss = event.target.closest('[data-dismiss-message]');
  // Eemalda ainult selle nupuga seotud teade lehelt.
  if (dismiss) dismiss.closest('.message').remove();
});
