const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const test = require('node:test');

const source = fs.readFileSync(path.join(__dirname, '../../assets/js/wildlife-gallery.js'), 'utf8');

// A small DOM test double exercises state transitions without a browser or network.
function element(properties = {}) {
  return Object.assign({
    hidden: false, value: '', dataset: {}, textContent: '', listeners: {}, selectors: {},
    addEventListener(name, handler) { this.listeners[name] = handler; },
    querySelector(selector) { return this.selectors[selector] || null; },
    querySelectorAll(selector) { return this.selectors[selector] || []; },
    fire(name, extra = {}) { this.listeners[name]({ currentTarget: this, preventDefault() {}, ...extra }); },
    focus() { this.focused = true; },
    removeAttribute(name) { delete this[name]; },
    replaceChildren() { this.children = []; },
    appendChild(child) { this.children.push(child); },
    cloneNode() { return { textContent: this.textContent }; },
  }, properties);
}

function run(document) {
  vm.runInNewContext(source, { document, window: { location: {} } });
}

test('species search, combined filters, pagination, and no-results state', () => {
  const cards = Array.from({ length: 35 }, (_, index) => element({ dataset: {
    name: index < 30 ? `Owl ${index}` : `Fox ${index}`,
    category: index < 30 ? 'Birds' : 'Mammals',
    group: index < 30 ? 'Raptors & Owls' : '',
  }}));
  const selectors = {};
  ['species-search', 'category-filter', 'group-filter', 'bird-group-label',
    'species-more', 'species-empty', 'species-results'].forEach(name => {
    selectors[`[data-${name}]`] = element();
  });
  selectors['.wildlife-filters'] = element({ hidden: true });
  selectors['[data-gallery-highlights]'] = element();
  selectors['[data-species-card]'] = cards;
  const browser = element({ selectors });
  run({ querySelector(selector) { return selector === '[data-species-browser]' ? browser : null; } });
  const get = name => selectors[`[data-${name}]`];
  assert.equal(cards.filter(card => !card.hidden).length, 24);
  assert.equal(selectors['[data-gallery-highlights]'].hidden, false);
  get('species-more').fire('click');
  assert.equal(cards.filter(card => !card.hidden).length, 35);
  get('category-filter').value = 'Mammals';
  get('category-filter').fire('change');
  assert.equal(cards.filter(card => !card.hidden).length, 5);
  assert.equal(get('bird-group-label').hidden, true);
  assert.equal(selectors['[data-gallery-highlights]'].hidden, true);
  get('species-search').value = 'nothing matches';
  get('species-search').fire('input');
  assert.equal(cards.filter(card => !card.hidden).length, 0);
  assert.equal(get('species-empty').hidden, false);
  get('species-search').value = '';
  get('category-filter').value = 'Birds';
  get('category-filter').fire('change');
  assert.equal(cards.filter(card => !card.hidden).length, 24);
  assert.equal(get('bird-group-label').hidden, false);
  get('group-filter').value = 'Raptors & Owls';
  get('group-filter').fire('change');
  get('species-search').value = 'Owl 29';
  get('species-search').fire('input');
  assert.equal(cards.filter(card => !card.hidden).length, 1);
  get('species-search').value = '';
  get('group-filter').value = '';
  get('category-filter').value = '';
  get('category-filter').fire('change');
  assert.equal(selectors['[data-gallery-highlights]'].hidden, false);
  get('species-search').value = 'Owl';
  get('species-search').fire('input');
  assert.equal(selectors['[data-gallery-highlights]'].hidden, true);
  get('species-search').value = '';
  get('species-search').fire('input');
  assert.equal(selectors['[data-gallery-highlights]'].hidden, false);
});

test('country, state, and place cascade and combine with species filters', () => {
  const california = { name: 'Descanso Gardens, California', country: 'United States', state: 'California' };
  const pasadena = { name: 'Pasadena, California', country: 'United States', state: 'California' };
  const hawaii = { name: 'Maui, Hawaii', country: 'United States', state: 'Hawaii' };
  const canada = { name: 'Toronto, Ontario', country: 'Canada', state: 'Ontario' };
  const wisconsin = { name: 'Madison, Wisconsin', country: 'United States', state: 'Wisconsin' };
  const cards = [
    ['Owl California', 'Birds', [california]],
    ['Owl traveler', 'Birds', [california, pasadena, hawaii]],
    ['Finch Hawaii', 'Birds', [hawaii]],
    ['Fox Canada', 'Mammals', [canada]],
    ['Crane Wisconsin', 'Birds', [wisconsin]],
  ].map(([name, category, locations]) => element({ dataset: {
    name, category, group: name.startsWith('Owl') ? 'Raptors & Owls' : '',
    locations: JSON.stringify(locations),
  }}));
  const selectors = {};
  ['species-search', 'category-filter', 'group-filter', 'country-filter', 'state-filter',
    'place-filter', 'bird-group-label', 'species-more', 'species-empty', 'species-results',
    'gallery-highlights'].forEach(name => { selectors[`[data-${name}]`] = element(); });
  selectors['.wildlife-filters'] = element({ hidden: true });
  selectors['[data-species-card]'] = cards;
  const browser = element({ selectors });
  run({
    querySelector(selector) { return selector === '[data-species-browser]' ? browser : null; },
    createElement() { return element(); },
  });
  const get = name => selectors[`[data-${name}]`];
  const choose = (name, value) => { get(name).value = value; get(name).fire(name === 'species-search' ? 'input' : 'change'); };
  const visible = () => cards.filter(card => !card.hidden).map(card => card.dataset.name);
  const choices = name => get(name).children.map(option => option.value);
  assert.deepEqual(choices('country-filter'), ['', 'Canada', 'United States']);
  assert.equal(get('country-filter').children.find(x => x.value === 'United States').textContent, 'United States (4)');
  assert.equal(get('state-filter').children.find(x => x.value === 'California').textContent, 'California (2)');
  choose('country-filter', 'United States');
  assert.equal(visible().length, 4);
  assert.equal(get('gallery-highlights').hidden, true);
  assert.equal(choices('state-filter').includes('Ontario'), false);
  choose('state-filter', 'California');
  assert.deepEqual(visible(), ['Owl California', 'Owl traveler']);
  assert.equal(choices('place-filter').includes('Maui, Hawaii'), false);
  // Even an inconsistent stale place must not match a different location in the same album.
  choose('place-filter', 'Maui, Hawaii');
  assert.equal(visible().length, 0);
  choose('place-filter', 'Descanso Gardens, California');
  choose('state-filter', 'Hawaii');
  assert.equal(get('place-filter').value, '');
  assert.deepEqual(visible(), ['Owl traveler', 'Finch Hawaii']);
  choose('place-filter', 'Maui, Hawaii');
  choose('species-search', 'owl');
  assert.deepEqual(visible(), ['Owl traveler']);
  choose('category-filter', 'Mammals');
  assert.equal(visible().length, 0);
  assert.equal(get('species-empty').hidden, false);
  choose('species-search', '');
  choose('category-filter', '');
  choose('country-filter', 'Canada');
  assert.equal(get('state-filter').value, '');
  assert.equal(get('place-filter').value, '');
  assert.deepEqual(visible(), ['Fox Canada']);
  assert.deepEqual(choices('state-filter'), ['', 'Ontario']);
  choose('country-filter', '');
  assert.equal(visible().length, 5);
  assert.equal(get('gallery-highlights').hidden, false);
  // A place may also be chosen directly, without first choosing a country or state.
  choose('place-filter', 'Maui, Hawaii');
  assert.deepEqual(visible(), ['Owl traveler', 'Finch Hawaii']);
});

test('150-photo album loads in batches; viewer retains camera info and keyboard navigation', () => {
  const photos = Array.from({ length: 150 }, (_, index) => element({ selectors: {
    '[data-open-photo]': element({ dataset: { full: `/photo_gallery/owl/${index}.jpg`, alt: `Great Horned Owl — Juvenile ${index}` }}),
    '.wildlife-caption': element({ textContent: `Owl ${index}` }),
    '.wildlife-photo-context': element({ textContent: 'California · November 14, 2026' }),
    '[data-camera-info]': element({ textContent: 'Sony · 600mm f/6.3 1/1250 ISO 100' }),
  }}));
  const viewer = element({ selectors: {} });
  ['image', 'caption', 'context', 'camera', 'count', 'original', 'previous', 'next', 'close']
    .forEach(name => { viewer.selectors[`[data-viewer-${name}]`] = element(); });
  viewer.showModal = function () { this.open = true; };
  viewer.close = function () { this.open = false; this.fire('close'); };
  const album = element({ selectors: {
    '[data-photo]': photos,
    '[data-photos-more]': element(),
    '[data-photo-results]': element(),
    '[data-photo-viewer]': viewer,
  }});
  run({ querySelector(selector) { return selector === '[data-species-album]' ? album : null; } });
  assert.equal(photos.filter(photo => !photo.hidden).length, 24);
  album.querySelector('[data-photos-more]').fire('click');
  assert.equal(photos.filter(photo => !photo.hidden).length, 48);
  const opener = photos[0].querySelector('[data-open-photo]');
  opener.fire('click');
  assert.equal(viewer.open, true);
  assert.equal(viewer.querySelector('[data-viewer-image]').src, '/photo_gallery/owl/0.jpg');
  assert.equal(viewer.querySelector('[data-viewer-image]').alt, 'Great Horned Owl — Juvenile 0');
  assert.match(viewer.querySelector('[data-viewer-camera]').children[0].textContent, /600mm/);
  assert.equal(viewer.querySelector('[data-viewer-previous]').disabled, true);
  viewer.fire('keydown', { key: 'ArrowRight' });
  assert.equal(viewer.querySelector('[data-viewer-caption]').textContent, 'Owl 1');
  assert.equal(viewer.querySelector('[data-viewer-image]').alt, 'Great Horned Owl — Juvenile 1');
  viewer.querySelector('[data-viewer-close]').fire('click');
  assert.equal(viewer.open, false);
  assert.equal(opener.focused, true);
  assert.equal(viewer.querySelector('[data-viewer-image]').src, undefined);
  for (let index = 0; index < 6; index++) album.querySelector('[data-photos-more]').fire('click');
  assert.equal(photos.filter(photo => !photo.hidden).length, 150);
  assert.equal(album.querySelector('[data-photos-more]').hidden, true);
});
