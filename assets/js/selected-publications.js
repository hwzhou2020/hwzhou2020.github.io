/* Native buttons and disclosures keep the complete publication text available. */
document.addEventListener('DOMContentLoaded', function () {
  var grid = document.querySelector('.selected-publications-grid');
  var filters = document.querySelectorAll('.publication-filter');
  if (!grid || !filters.length) return;

  filters.forEach(function (button) {
    button.addEventListener('click', function () {
      var topic = button.getAttribute('data-topic');
      grid.setAttribute('data-filter', topic);
      filters.forEach(function (filter) {
        var selected = filter === button;
        filter.classList.toggle('active', selected);
        filter.setAttribute('aria-pressed', String(selected));
      });
      grid.querySelectorAll('.publication').forEach(function (paper) {
        paper.hidden = topic !== 'all' && paper.getAttribute('data-topic') !== topic;
      });
      var count = grid.querySelectorAll('.publication:not([hidden])').length;
      document.getElementById('selected-publication-count').textContent =
        count + (count === 1 ? ' paper' : ' papers');
    });
  });

  if (typeof HTMLDialogElement === 'undefined') return;
  var dialog = document.createElement('dialog');
  dialog.className = 'publication-figure-dialog';
  dialog.setAttribute('aria-label', 'Publication figure');
  var close = document.createElement('button');
  close.type = 'button';
  close.className = 'figure-close';
  close.textContent = 'Close image';
  close.autofocus = true;
  var enlarged = document.createElement('img');
  var caption = document.createElement('p');
  caption.className = 'figure-caption';
  dialog.appendChild(close);
  dialog.appendChild(enlarged);
  dialog.appendChild(caption);
  document.body.appendChild(dialog);
  close.addEventListener('click', function () { dialog.close(); });
  dialog.addEventListener('click', function (event) {
    if (event.target === dialog) dialog.close();
  });
  grid.querySelectorAll('.publication-image img').forEach(function (image) {
    var title = image.closest('.publication').querySelector('.publication-title').textContent.trim();
    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'publication-figure-button';
    button.setAttribute('aria-label', 'Enlarge figure: ' + title);
    button.setAttribute('aria-haspopup', 'dialog');
    image.parentNode.insertBefore(button, image);
    button.appendChild(image);
    button.addEventListener('click', function () {
      enlarged.src = image.currentSrc || image.src;
      enlarged.alt = image.alt;
      caption.textContent = title;
      dialog.showModal();
    });
  });
});
