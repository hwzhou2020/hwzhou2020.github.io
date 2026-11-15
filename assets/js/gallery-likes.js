(function () {
  var COUNTER_API_BASE = 'https://api.counterapi.dev/v1';
  var gallery = document.querySelector('[data-counter-namespace]');
  if (!gallery) { return; }
  var COUNTER_NAMESPACE = gallery.dataset.counterNamespace;
  var LOCAL_LIKES_STORAGE_KEY = 'gallery-likes-cache-v2';

  function getLikesStorage() {
    try {
      if (!window.localStorage) { return null; }
      var probeKey = '__gallery_likes_probe__';
      window.localStorage.setItem(probeKey, '1');
      window.localStorage.removeItem(probeKey);
      return window.localStorage;
    } catch (error) {
      return null;
    }
  }

  var likesStorage = getLikesStorage();

  function loadStoredLikes() {
    if (!likesStorage) { return {}; }
    try {
      var raw = likesStorage.getItem(LOCAL_LIKES_STORAGE_KEY);
      if (!raw) { return {}; }
      var parsed = JSON.parse(raw);
      return parsed && typeof parsed === 'object' ? parsed : {};
    } catch (error) {
      return {};
    }
  }

  var storedLikes = loadStoredLikes();

  function readStoredEntry(counterName) {
    var entry = storedLikes[counterName];
    if (!entry || typeof entry !== 'object') {
      return { total: 0, pending: 0 };
    }

    var total = typeof entry.total === 'number' && entry.total >= 0 ? entry.total : 0;
    var pending = typeof entry.pending === 'number' && entry.pending >= 0 ? Math.floor(entry.pending) : 0;
    return {
      total: Math.max(0, total),
      pending: pending
    };
  }

  function persistStoredEntry(counterName, total, pending) {
    if (!likesStorage) { return; }

    storedLikes[counterName] = {
      total: Math.max(0, total),
      pending: Math.max(0, Math.floor(pending || 0))
    };

    try {
      likesStorage.setItem(LOCAL_LIKES_STORAGE_KEY, JSON.stringify(storedLikes));
    } catch (error) {
      console.error('Error caching likes for', counterName, error);
    }
  }

  function renderCount(countEl, value) {
    countEl.textContent = value > 0 ? String(value) : '';
  }

  function extractCounterValue(data) {
    if (typeof data.count === 'number') { return data.count; }
    if (typeof data.value === 'number') { return data.value; }
    if (data.data && typeof data.data.count === 'number') { return data.data.count; }
    if (data.data && typeof data.data.value === 'number') { return data.data.value; }
    return 0;
  }

  function counterUrl(counterName, action) {
    var path = [COUNTER_API_BASE, encodeURIComponent(COUNTER_NAMESPACE), encodeURIComponent(counterName)].join('/');
    var endpoint = action ? path + '/' + action : path + '/';
    return endpoint + '?ts=' + Date.now();
  }

  function readCounter(counterName) {
    return fetch(counterUrl(counterName), { method: 'GET', cache: 'no-store' })
      .then(function (response) {
        if (!response.ok) { throw new Error('Failed to load counter'); }
        return response.json();
      })
      .then(function (data) {
        return extractCounterValue(data);
      });
  }

  function incrementCounter(counterName) {
    return fetch(counterUrl(counterName, 'up'), { method: 'GET', cache: 'no-store' })
      .then(function (response) {
        if (!response.ok) { throw new Error('Failed to increment counter'); }
        return response.json();
      })
      .then(function (data) {
        return extractCounterValue(data);
      });
  }

  function initButton(btn) {
    var counterName = btn.dataset.counter;
    var countEl = btn.querySelector('.heart-count');
    var storedEntry = readStoredEntry(counterName);
    var state = {
      baseCount: 0,
      displayCount: storedEntry.total,
      pending: storedEntry.pending,
      queue: Promise.resolve()
    };

    function syncDisplay() {
      renderCount(countEl, state.displayCount);
    }

    function persistState() {
      persistStoredEntry(counterName, state.displayCount, state.pending);
    }

    function flashButton() {
      btn.classList.remove('pop', 'bumped');
      void btn.offsetWidth;
      btn.classList.add('pop', 'bumped');
      window.setTimeout(function () {
        btn.classList.remove('bumped');
      }, 320);
    }

    function flushPendingLikes() {
      if (state.pending <= 0) {
        persistState();
        return Promise.resolve();
      }

      return incrementCounter(counterName)
        .then(function (value) {
          state.pending = Math.max(0, state.pending - 1);
          state.baseCount = Math.max(state.baseCount + 1, value);
          state.displayCount = Math.max(state.displayCount, state.baseCount + state.pending);
          syncDisplay();
          persistState();
          return flushPendingLikes();
        })
        .catch(function (error) {
          syncDisplay();
          persistState();
          console.error('Error incrementing counter for', counterName, error);
          throw error;
        });
    }

    syncDisplay();
    persistState();

    state.queue = readCounter(counterName)
      .then(function (value) {
        state.baseCount = value;
        state.displayCount = Math.max(state.displayCount, state.baseCount + state.pending);
        syncDisplay();
        persistState();
        return flushPendingLikes();
      })
      .catch(function (error) {
        syncDisplay();
        persistState();
        console.error('Error loading counter for', counterName, error);
        return flushPendingLikes().catch(function () {});
      });

    btn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();

      state.pending += 1;
      state.displayCount += 1;
      syncDisplay();
      persistState();
      flashButton();

      state.queue = state.queue
        .catch(function () {})
        .then(flushPendingLikes);
    });
  }

  var buttons = gallery.querySelectorAll('.photo-heart');
  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          observer.unobserve(entry.target);
          initButton(entry.target);
        }
      });
    });
    buttons.forEach(function (button) { observer.observe(button); });
  } else {
    buttons.forEach(initButton);
  }
})();
