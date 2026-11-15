(function () {
  'use strict';
  var batchSize = 24;
  var browser = document.querySelector('[data-species-browser]');
  if (browser) {
    var cards = Array.from(browser.querySelectorAll('[data-species-card]'));
    var search = browser.querySelector('[data-species-search]');
    var category = browser.querySelector('[data-category-filter]');
    var group = browser.querySelector('[data-group-filter]');
    var location = browser.querySelector('[data-location-filter]');
    var highlights = browser.querySelector('[data-gallery-highlights]');
    var more = browser.querySelector('[data-species-more]');
    var limit = batchSize;
    function filterSpecies() {
      var query = search.value.trim().toLocaleLowerCase();
      var birdGroupsAvailable = !category.value || category.value === 'Birds';
      browser.querySelector('[data-bird-group-label]').hidden = !birdGroupsAvailable;
      if (!birdGroupsAvailable) { group.value = ''; }
      if (highlights) {
        highlights.hidden = Boolean(query || category.value || group.value || (location && location.value));
      }
      var matches = cards.filter(function (card) {
        return card.dataset.name.toLocaleLowerCase().includes(query) &&
          (!category.value || card.dataset.category === category.value) &&
          (!group.value || card.dataset.group === group.value) &&
          (!location || !location.value || JSON.parse(card.dataset.locations).includes(location.value));
      });
      cards.forEach(function (card) { card.hidden = true; });
      matches.slice(0, limit).forEach(function (card) { card.hidden = false; });
      browser.querySelector('[data-species-results]').textContent =
        'Showing ' + Math.min(limit, matches.length) + ' of ' + matches.length + ' albums';
      browser.querySelector('[data-species-empty]').hidden = matches.length !== 0;
      more.hidden = limit >= matches.length;
    }
    [search, category, group, location].filter(Boolean).forEach(function (control) {
      control.addEventListener(control === search ? 'input' : 'change', function () {
        limit = batchSize;
        filterSpecies();
      });
    });
    more.addEventListener('click', function () { limit += batchSize; filterSpecies(); });
    browser.querySelector('.wildlife-filters').hidden = false;
    filterSpecies();
  }

  var album = document.querySelector('[data-species-album]');
  if (!album) { return; }
  var photos = Array.from(album.querySelectorAll('[data-photo]'));
  var photoLimit = batchSize;
  var photoMore = album.querySelector('[data-photos-more]');
  function showPhotos() {
    photos.forEach(function (photo, index) { photo.hidden = index >= photoLimit; });
    album.querySelector('[data-photo-results]').textContent =
      'Showing ' + Math.min(photoLimit, photos.length) + ' of ' + photos.length + ' photographs';
    photoMore.hidden = photoLimit >= photos.length;
  }
  photoMore.addEventListener('click', function () { photoLimit += batchSize; showPhotos(); });
  showPhotos();

  var viewer = album.querySelector('[data-photo-viewer]');
  var viewerImage = viewer.querySelector('[data-viewer-image]');
  var currentIndex = 0;
  var opener = null;
  function displayPhoto(index) {
    currentIndex = index;
    var photo = photos[index];
    var button = photo.querySelector('[data-open-photo]');
    var caption = photo.querySelector('.wildlife-caption').textContent;
    var camera = photo.querySelector('[data-camera-info]');
    viewerImage.src = button.dataset.full;
    viewerImage.alt = caption;
    viewer.querySelector('[data-viewer-caption]').textContent = caption;
    viewer.querySelector('[data-viewer-context]').textContent = photo.querySelector('.wildlife-photo-context').textContent;
    // A clone retains the line break between equipment and exposure settings.
    var cameraTarget = viewer.querySelector('[data-viewer-camera]');
    cameraTarget.replaceChildren();
    if (camera) { cameraTarget.appendChild(camera.cloneNode(true)); }
    viewer.querySelector('[data-viewer-count]').textContent = (index + 1) + ' / ' + photos.length;
    viewer.querySelector('[data-viewer-original]').href = button.dataset.full;
    viewer.querySelector('[data-viewer-previous]').disabled = index === 0;
    viewer.querySelector('[data-viewer-next]').disabled = index === photos.length - 1;
  }
  photos.forEach(function (photo, index) {
    photo.querySelector('[data-open-photo]').addEventListener('click', function (event) {
      if (typeof viewer.showModal !== 'function') {
        window.location.href = event.currentTarget.dataset.full;
        return;
      }
      opener = event.currentTarget;
      displayPhoto(index);
      viewer.showModal();
    });
  });
  viewer.querySelector('[data-viewer-close]').addEventListener('click', function () { viewer.close(); });
  viewer.querySelector('[data-viewer-previous]').addEventListener('click', function () {
    if (currentIndex > 0) { displayPhoto(currentIndex - 1); }
  });
  viewer.querySelector('[data-viewer-next]').addEventListener('click', function () {
    if (currentIndex < photos.length - 1) { displayPhoto(currentIndex + 1); }
  });
  viewer.addEventListener('keydown', function (event) {
    if (event.key === 'ArrowLeft' && currentIndex > 0) { event.preventDefault(); displayPhoto(currentIndex - 1); }
    if (event.key === 'ArrowRight' && currentIndex < photos.length - 1) { event.preventDefault(); displayPhoto(currentIndex + 1); }
  });
  viewer.addEventListener('click', function (event) {
    var bounds = viewer.getBoundingClientRect();
    if (event.target === viewer && (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom)) {
      viewer.close();
    }
  });
  viewer.addEventListener('close', function () {
    viewerImage.removeAttribute('src');
    if (opener) { opener.focus(); }
  });
})();
