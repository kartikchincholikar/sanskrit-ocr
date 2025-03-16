/******/ (() => { // webpackBootstrap
/******/ 	"use strict";

;// ./src/fragmentLoader.js
function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
function _regeneratorRuntime() { "use strict"; /*! regenerator-runtime -- Copyright (c) 2014-present, Facebook, Inc. -- license (MIT): https://github.com/facebook/regenerator/blob/main/LICENSE */ _regeneratorRuntime = function _regeneratorRuntime() { return e; }; var t, e = {}, r = Object.prototype, n = r.hasOwnProperty, o = Object.defineProperty || function (t, e, r) { t[e] = r.value; }, i = "function" == typeof Symbol ? Symbol : {}, a = i.iterator || "@@iterator", c = i.asyncIterator || "@@asyncIterator", u = i.toStringTag || "@@toStringTag"; function define(t, e, r) { return Object.defineProperty(t, e, { value: r, enumerable: !0, configurable: !0, writable: !0 }), t[e]; } try { define({}, ""); } catch (t) { define = function define(t, e, r) { return t[e] = r; }; } function wrap(t, e, r, n) { var i = e && e.prototype instanceof Generator ? e : Generator, a = Object.create(i.prototype), c = new Context(n || []); return o(a, "_invoke", { value: makeInvokeMethod(t, r, c) }), a; } function tryCatch(t, e, r) { try { return { type: "normal", arg: t.call(e, r) }; } catch (t) { return { type: "throw", arg: t }; } } e.wrap = wrap; var h = "suspendedStart", l = "suspendedYield", f = "executing", s = "completed", y = {}; function Generator() {} function GeneratorFunction() {} function GeneratorFunctionPrototype() {} var p = {}; define(p, a, function () { return this; }); var d = Object.getPrototypeOf, v = d && d(d(values([]))); v && v !== r && n.call(v, a) && (p = v); var g = GeneratorFunctionPrototype.prototype = Generator.prototype = Object.create(p); function defineIteratorMethods(t) { ["next", "throw", "return"].forEach(function (e) { define(t, e, function (t) { return this._invoke(e, t); }); }); } function AsyncIterator(t, e) { function invoke(r, o, i, a) { var c = tryCatch(t[r], t, o); if ("throw" !== c.type) { var u = c.arg, h = u.value; return h && "object" == _typeof(h) && n.call(h, "__await") ? e.resolve(h.__await).then(function (t) { invoke("next", t, i, a); }, function (t) { invoke("throw", t, i, a); }) : e.resolve(h).then(function (t) { u.value = t, i(u); }, function (t) { return invoke("throw", t, i, a); }); } a(c.arg); } var r; o(this, "_invoke", { value: function value(t, n) { function callInvokeWithMethodAndArg() { return new e(function (e, r) { invoke(t, n, e, r); }); } return r = r ? r.then(callInvokeWithMethodAndArg, callInvokeWithMethodAndArg) : callInvokeWithMethodAndArg(); } }); } function makeInvokeMethod(e, r, n) { var o = h; return function (i, a) { if (o === f) throw Error("Generator is already running"); if (o === s) { if ("throw" === i) throw a; return { value: t, done: !0 }; } for (n.method = i, n.arg = a;;) { var c = n.delegate; if (c) { var u = maybeInvokeDelegate(c, n); if (u) { if (u === y) continue; return u; } } if ("next" === n.method) n.sent = n._sent = n.arg;else if ("throw" === n.method) { if (o === h) throw o = s, n.arg; n.dispatchException(n.arg); } else "return" === n.method && n.abrupt("return", n.arg); o = f; var p = tryCatch(e, r, n); if ("normal" === p.type) { if (o = n.done ? s : l, p.arg === y) continue; return { value: p.arg, done: n.done }; } "throw" === p.type && (o = s, n.method = "throw", n.arg = p.arg); } }; } function maybeInvokeDelegate(e, r) { var n = r.method, o = e.iterator[n]; if (o === t) return r.delegate = null, "throw" === n && e.iterator["return"] && (r.method = "return", r.arg = t, maybeInvokeDelegate(e, r), "throw" === r.method) || "return" !== n && (r.method = "throw", r.arg = new TypeError("The iterator does not provide a '" + n + "' method")), y; var i = tryCatch(o, e.iterator, r.arg); if ("throw" === i.type) return r.method = "throw", r.arg = i.arg, r.delegate = null, y; var a = i.arg; return a ? a.done ? (r[e.resultName] = a.value, r.next = e.nextLoc, "return" !== r.method && (r.method = "next", r.arg = t), r.delegate = null, y) : a : (r.method = "throw", r.arg = new TypeError("iterator result is not an object"), r.delegate = null, y); } function pushTryEntry(t) { var e = { tryLoc: t[0] }; 1 in t && (e.catchLoc = t[1]), 2 in t && (e.finallyLoc = t[2], e.afterLoc = t[3]), this.tryEntries.push(e); } function resetTryEntry(t) { var e = t.completion || {}; e.type = "normal", delete e.arg, t.completion = e; } function Context(t) { this.tryEntries = [{ tryLoc: "root" }], t.forEach(pushTryEntry, this), this.reset(!0); } function values(e) { if (e || "" === e) { var r = e[a]; if (r) return r.call(e); if ("function" == typeof e.next) return e; if (!isNaN(e.length)) { var o = -1, i = function next() { for (; ++o < e.length;) if (n.call(e, o)) return next.value = e[o], next.done = !1, next; return next.value = t, next.done = !0, next; }; return i.next = i; } } throw new TypeError(_typeof(e) + " is not iterable"); } return GeneratorFunction.prototype = GeneratorFunctionPrototype, o(g, "constructor", { value: GeneratorFunctionPrototype, configurable: !0 }), o(GeneratorFunctionPrototype, "constructor", { value: GeneratorFunction, configurable: !0 }), GeneratorFunction.displayName = define(GeneratorFunctionPrototype, u, "GeneratorFunction"), e.isGeneratorFunction = function (t) { var e = "function" == typeof t && t.constructor; return !!e && (e === GeneratorFunction || "GeneratorFunction" === (e.displayName || e.name)); }, e.mark = function (t) { return Object.setPrototypeOf ? Object.setPrototypeOf(t, GeneratorFunctionPrototype) : (t.__proto__ = GeneratorFunctionPrototype, define(t, u, "GeneratorFunction")), t.prototype = Object.create(g), t; }, e.awrap = function (t) { return { __await: t }; }, defineIteratorMethods(AsyncIterator.prototype), define(AsyncIterator.prototype, c, function () { return this; }), e.AsyncIterator = AsyncIterator, e.async = function (t, r, n, o, i) { void 0 === i && (i = Promise); var a = new AsyncIterator(wrap(t, r, n, o), i); return e.isGeneratorFunction(r) ? a : a.next().then(function (t) { return t.done ? t.value : a.next(); }); }, defineIteratorMethods(g), define(g, u, "Generator"), define(g, a, function () { return this; }), define(g, "toString", function () { return "[object Generator]"; }), e.keys = function (t) { var e = Object(t), r = []; for (var n in e) r.push(n); return r.reverse(), function next() { for (; r.length;) { var t = r.pop(); if (t in e) return next.value = t, next.done = !1, next; } return next.done = !0, next; }; }, e.values = values, Context.prototype = { constructor: Context, reset: function reset(e) { if (this.prev = 0, this.next = 0, this.sent = this._sent = t, this.done = !1, this.delegate = null, this.method = "next", this.arg = t, this.tryEntries.forEach(resetTryEntry), !e) for (var r in this) "t" === r.charAt(0) && n.call(this, r) && !isNaN(+r.slice(1)) && (this[r] = t); }, stop: function stop() { this.done = !0; var t = this.tryEntries[0].completion; if ("throw" === t.type) throw t.arg; return this.rval; }, dispatchException: function dispatchException(e) { if (this.done) throw e; var r = this; function handle(n, o) { return a.type = "throw", a.arg = e, r.next = n, o && (r.method = "next", r.arg = t), !!o; } for (var o = this.tryEntries.length - 1; o >= 0; --o) { var i = this.tryEntries[o], a = i.completion; if ("root" === i.tryLoc) return handle("end"); if (i.tryLoc <= this.prev) { var c = n.call(i, "catchLoc"), u = n.call(i, "finallyLoc"); if (c && u) { if (this.prev < i.catchLoc) return handle(i.catchLoc, !0); if (this.prev < i.finallyLoc) return handle(i.finallyLoc); } else if (c) { if (this.prev < i.catchLoc) return handle(i.catchLoc, !0); } else { if (!u) throw Error("try statement without catch or finally"); if (this.prev < i.finallyLoc) return handle(i.finallyLoc); } } } }, abrupt: function abrupt(t, e) { for (var r = this.tryEntries.length - 1; r >= 0; --r) { var o = this.tryEntries[r]; if (o.tryLoc <= this.prev && n.call(o, "finallyLoc") && this.prev < o.finallyLoc) { var i = o; break; } } i && ("break" === t || "continue" === t) && i.tryLoc <= e && e <= i.finallyLoc && (i = null); var a = i ? i.completion : {}; return a.type = t, a.arg = e, i ? (this.method = "next", this.next = i.finallyLoc, y) : this.complete(a); }, complete: function complete(t, e) { if ("throw" === t.type) throw t.arg; return "break" === t.type || "continue" === t.type ? this.next = t.arg : "return" === t.type ? (this.rval = this.arg = t.arg, this.method = "return", this.next = "end") : "normal" === t.type && e && (this.next = e), y; }, finish: function finish(t) { for (var e = this.tryEntries.length - 1; e >= 0; --e) { var r = this.tryEntries[e]; if (r.finallyLoc === t) return this.complete(r.completion, r.afterLoc), resetTryEntry(r), y; } }, "catch": function _catch(t) { for (var e = this.tryEntries.length - 1; e >= 0; --e) { var r = this.tryEntries[e]; if (r.tryLoc === t) { var n = r.completion; if ("throw" === n.type) { var o = n.arg; resetTryEntry(r); } return o; } } throw Error("illegal catch attempt"); }, delegateYield: function delegateYield(e, r, n) { return this.delegate = { iterator: values(e), resultName: r, nextLoc: n }, "next" === this.method && (this.arg = t), y; } }, e; }
function _classCallCheck(a, n) { if (!(a instanceof n)) throw new TypeError("Cannot call a class as a function"); }
function _defineProperties(e, r) { for (var t = 0; t < r.length; t++) { var o = r[t]; o.enumerable = o.enumerable || !1, o.configurable = !0, "value" in o && (o.writable = !0), Object.defineProperty(e, _toPropertyKey(o.key), o); } }
function _createClass(e, r, t) { return r && _defineProperties(e.prototype, r), t && _defineProperties(e, t), Object.defineProperty(e, "prototype", { writable: !1 }), e; }
function _toPropertyKey(t) { var i = _toPrimitive(t, "string"); return "symbol" == _typeof(i) ? i : i + ""; }
function _toPrimitive(t, r) { if ("object" != _typeof(t) || !t) return t; var e = t[Symbol.toPrimitive]; if (void 0 !== e) { var i = e.call(t, r || "default"); if ("object" != _typeof(i)) return i; throw new TypeError("@@toPrimitive must return a primitive value."); } return ("string" === r ? String : Number)(t); }
function asyncGeneratorStep(n, t, e, r, o, a, c) { try { var i = n[a](c), u = i.value; } catch (n) { return void e(n); } i.done ? t(u) : Promise.resolve(u).then(r, o); }
function _asyncToGenerator(n) { return function () { var t = this, e = arguments; return new Promise(function (r, o) { var a = n.apply(t, e); function _next(n) { asyncGeneratorStep(a, r, o, _next, _throw, "next", n); } function _throw(n) { asyncGeneratorStep(a, r, o, _next, _throw, "throw", n); } _next(void 0); }); }; }
function loadFragments() {
  return _loadFragments.apply(this, arguments);
}
function _loadFragments() {
  _loadFragments = _asyncToGenerator(/*#__PURE__*/_regeneratorRuntime().mark(function _callee7() {
    var fragmentElements, FetchQueue, fetchQueue, currentIndex, elements;
    return _regeneratorRuntime().wrap(function _callee7$(_context7) {
      while (1) switch (_context7.prev = _context7.next) {
        case 0:
          // Find all elements with ids starting with 'fragment-'
          fragmentElements = Array.from(document.querySelectorAll('[id^="fragment-"]'));
          FetchQueue = /*#__PURE__*/function () {
            function FetchQueue() {
              var maxConcurrent = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : 3;
              _classCallCheck(this, FetchQueue);
              this.queue = [];
              this.maxConcurrent = maxConcurrent;
              this.activeFetches = 0;
              this.maxRetries = 3; // Maximum number of retry attempts
              this.baseDelay = 1000; // Base delay in milliseconds (1 second)
            }
            return _createClass(FetchQueue, [{
              key: "sleep",
              value: function () {
                var _sleep = _asyncToGenerator(/*#__PURE__*/_regeneratorRuntime().mark(function _callee(ms) {
                  return _regeneratorRuntime().wrap(function _callee$(_context) {
                    while (1) switch (_context.prev = _context.next) {
                      case 0:
                        return _context.abrupt("return", new Promise(function (resolve) {
                          return setTimeout(resolve, ms);
                        }));
                      case 1:
                      case "end":
                        return _context.stop();
                    }
                  }, _callee);
                }));
                function sleep(_x) {
                  return _sleep.apply(this, arguments);
                }
                return sleep;
              }()
            }, {
              key: "fetchWithRetry",
              value: function () {
                var _fetchWithRetry = _asyncToGenerator(/*#__PURE__*/_regeneratorRuntime().mark(function _callee2(fragmentPath) {
                  var retryCount,
                    response,
                    delay,
                    _args2 = arguments;
                  return _regeneratorRuntime().wrap(function _callee2$(_context2) {
                    while (1) switch (_context2.prev = _context2.next) {
                      case 0:
                        retryCount = _args2.length > 1 && _args2[1] !== undefined ? _args2[1] : 0;
                        _context2.prev = 1;
                        _context2.next = 4;
                        return fetch(fragmentPath);
                      case 4:
                        response = _context2.sent;
                        if (response.ok) {
                          _context2.next = 7;
                          break;
                        }
                        throw new Error("HTTP error! status: ".concat(response.status));
                      case 7:
                        _context2.next = 9;
                        return response.text();
                      case 9:
                        return _context2.abrupt("return", _context2.sent);
                      case 12:
                        _context2.prev = 12;
                        _context2.t0 = _context2["catch"](1);
                        if (!(retryCount < this.maxRetries)) {
                          _context2.next = 20;
                          break;
                        }
                        // Exponential backoff: 1s, 2s, 4s
                        delay = this.baseDelay * Math.pow(2, retryCount);
                        console.warn("Retry ".concat(retryCount + 1, "/").concat(this.maxRetries, " for ").concat(fragmentPath, " after ").concat(delay, "ms"));
                        _context2.next = 19;
                        return this.sleep(delay);
                      case 19:
                        return _context2.abrupt("return", this.fetchWithRetry(fragmentPath, retryCount + 1));
                      case 20:
                        throw _context2.t0;
                      case 21:
                      case "end":
                        return _context2.stop();
                    }
                  }, _callee2, this, [[1, 12]]);
                }));
                function fetchWithRetry(_x2) {
                  return _fetchWithRetry.apply(this, arguments);
                }
                return fetchWithRetry;
              }()
            }, {
              key: "addFetch",
              value: function () {
                var _addFetch = _asyncToGenerator(/*#__PURE__*/_regeneratorRuntime().mark(function _callee5(element) {
                  var _this = this;
                  var fragmentName, fragmentPath;
                  return _regeneratorRuntime().wrap(function _callee5$(_context5) {
                    while (1) switch (_context5.prev = _context5.next) {
                      case 0:
                        fragmentName = element.id.replace('fragment-', '');
                        fragmentPath = "fragments/".concat(fragmentName, ".html");
                        return _context5.abrupt("return", new Promise(/*#__PURE__*/function () {
                          var _ref = _asyncToGenerator(/*#__PURE__*/_regeneratorRuntime().mark(function _callee4(resolve, reject) {
                            var fetchPromise;
                            return _regeneratorRuntime().wrap(function _callee4$(_context4) {
                              while (1) switch (_context4.prev = _context4.next) {
                                case 0:
                                  try {
                                    fetchPromise = _asyncToGenerator(/*#__PURE__*/_regeneratorRuntime().mark(function _callee3() {
                                      var html, temp, scripts;
                                      return _regeneratorRuntime().wrap(function _callee3$(_context3) {
                                        while (1) switch (_context3.prev = _context3.next) {
                                          case 0:
                                            _context3.prev = 0;
                                            _context3.next = 3;
                                            return _this.fetchWithRetry(fragmentPath);
                                          case 3:
                                            html = _context3.sent;
                                            // Process the fragment
                                            temp = document.createElement('div');
                                            temp.innerHTML = html;
                                            element.innerHTML = temp.innerHTML;

                                            // Handle scripts
                                            scripts = temp.getElementsByTagName('script');
                                            Array.from(scripts).forEach(function (oldScript) {
                                              var newScript = document.createElement('script');
                                              Array.from(oldScript.attributes).forEach(function (attr) {
                                                newScript.setAttribute(attr.name, attr.value);
                                              });
                                              newScript.textContent = oldScript.textContent;
                                              oldScript.parentNode.removeChild(oldScript);
                                              document.body.appendChild(newScript);
                                            });
                                            _this.activeFetches--;
                                            resolve();
                                            _context3.next = 18;
                                            break;
                                          case 13:
                                            _context3.prev = 13;
                                            _context3.t0 = _context3["catch"](0);
                                            console.error("Failed to load fragment ".concat(fragmentPath, " after ").concat(_this.maxRetries, " retries:"), _context3.t0);
                                            _this.activeFetches--;
                                            reject(_context3.t0);
                                          case 18:
                                          case "end":
                                            return _context3.stop();
                                        }
                                      }, _callee3, null, [[0, 13]]);
                                    }))();
                                    _this.queue.push(fetchPromise);
                                    _this.activeFetches++;
                                  } catch (error) {
                                    reject(error);
                                  }
                                case 1:
                                case "end":
                                  return _context4.stop();
                              }
                            }, _callee4);
                          }));
                          return function (_x4, _x5) {
                            return _ref.apply(this, arguments);
                          };
                        }()));
                      case 3:
                      case "end":
                        return _context5.stop();
                    }
                  }, _callee5);
                }));
                function addFetch(_x3) {
                  return _addFetch.apply(this, arguments);
                }
                return addFetch;
              }()
            }, {
              key: "processNext",
              value: function () {
                var _processNext = _asyncToGenerator(/*#__PURE__*/_regeneratorRuntime().mark(function _callee6(element) {
                  return _regeneratorRuntime().wrap(function _callee6$(_context6) {
                    while (1) switch (_context6.prev = _context6.next) {
                      case 0:
                        if (!(this.activeFetches < this.maxConcurrent && element)) {
                          _context6.next = 3;
                          break;
                        }
                        _context6.next = 3;
                        return this.addFetch(element);
                      case 3:
                      case "end":
                        return _context6.stop();
                    }
                  }, _callee6, this);
                }));
                function processNext(_x6) {
                  return _processNext.apply(this, arguments);
                }
                return processNext;
              }()
            }]);
          }(); // Initialize queue
          fetchQueue = new FetchQueue(3);
          currentIndex = 0;
          elements = fragmentElements; // Assuming this is defined elsewhere
          // Initial loading of first 3 elements
        case 5:
          if (!(currentIndex < elements.length && currentIndex < 3)) {
            _context7.next = 11;
            break;
          }
          _context7.next = 8;
          return fetchQueue.processNext(elements[currentIndex]);
        case 8:
          currentIndex++;
          _context7.next = 5;
          break;
        case 11:
          if (!(currentIndex < elements.length)) {
            _context7.next = 20;
            break;
          }
          _context7.next = 14;
          return Promise.race(fetchQueue.queue);
        case 14:
          // Remove completed fetch from queue
          fetchQueue.queue = fetchQueue.queue.filter(function (p) {
            return p.status === 'pending';
          });
          // Add next element to queue
          _context7.next = 17;
          return fetchQueue.processNext(elements[currentIndex]);
        case 17:
          currentIndex++;
          _context7.next = 11;
          break;
        case 20:
          _context7.next = 22;
          return Promise.all(fetchQueue.queue);
        case 22:
        case "end":
          return _context7.stop();
      }
    }, _callee7);
  }));
  return _loadFragments.apply(this, arguments);
}

;// ./src/syncHFSpacesURLHash.js
var queryArg = "section";
function syncHFSpacesURLHash() {
  // Handle explicit section requests (don't update hash automatically on load)
  var hasExplicitRequest = handleExplicitSectionRequest();

  // Set up hash change monitoring
  updateHashBasedOnHashChange();

  // Always set up scroll monitoring to update hash during scrolling
  setupScrollMonitoring();

  // If no explicit request, we don't update the hash on initial load
  // The hash will only start updating when the user scrolls
}
function handleExplicitSectionRequest() {
  // Check for section parameter in URL
  var urlParams = new URLSearchParams(window.location.search);
  var sectionId = urlParams.get(queryArg);

  // If we have an explicit section request
  if (sectionId) {
    var targetElement = document.getElementById(sectionId);
    if (targetElement) {
      // Slight delay to ensure the browser doesn't try to do its own scrolling first
      setTimeout(function () {
        targetElement.scrollIntoView();
        history.replaceState(null, null, "#".concat(sectionId));
      }, 100);
    }
    return true;
  }

  // No explicit section parameter found
  return false;
}
function setupScrollMonitoring() {
  // Variables to manage throttling
  var isScrolling = false;
  var lastKnownScrollPosition = 0;
  var initialScroll = true;

  // Add the scroll event listener
  window.addEventListener('scroll', function () {
    lastKnownScrollPosition = window.scrollY;
    if (!isScrolling) {
      window.requestAnimationFrame(function () {
        // Skip the first scroll event which might be browser's automatic scroll
        // to a hash on page load
        if (initialScroll) {
          initialScroll = false;
        } else {
          updateHashBasedOnScroll(lastKnownScrollPosition);
        }
        isScrolling = false;
      });
    }
    isScrolling = true;
  });
}

// Function to update the URL hash based on scroll position
function updateHashBasedOnScroll(scrollPosition) {
  var closestHeading = findClosestHeading(scrollPosition);

  // Update the URL hash if we found a closest element
  if (closestHeading && closestHeading.id) {
    // Only update if the hash is different to avoid unnecessary operations
    if (window.location.hash !== "#".concat(closestHeading.id)) {
      silentlyUpdateHash(closestHeading.id);
      postMessageToHFSpaces(closestHeading.id);
    }
  }
}

// Find the closest heading to the current scroll position
function findClosestHeading(scrollPosition) {
  // Get only heading elements with IDs that we want to track
  var headingsWithIds = Array.from(document.querySelectorAll('h1[id], h2[id], h3[id], h4[id], h5[id], h6[id]'));

  // Skip if there are no headings with IDs
  if (headingsWithIds.length === 0) return null;

  // Find the element closest to the middle of the viewport
  var closestHeading = null;
  var closestDistance = Infinity;
  var viewportMiddle = scrollPosition + window.innerHeight / 2;

  // Iterate through all headings to find the closest one
  headingsWithIds.forEach(function (heading) {
    var headingTop = heading.getBoundingClientRect().top + scrollPosition;
    var distance = Math.abs(headingTop - viewportMiddle);
    if (distance < closestDistance) {
      closestDistance = distance;
      closestHeading = heading;
    }
  });
  return closestHeading;
}

// Update hash without triggering scroll or other side effects
function silentlyUpdateHash(id) {
  history.replaceState(null, null, "#".concat(id));
}
function updateHashBasedOnHashChange() {
  window.addEventListener('hashchange', function () {
    var elementId = window.location.hash.slice(1);
    postMessageToHFSpaces(elementId);
  });
}
function postMessageToHFSpaces(elementId) {
  var parentOrigin = "https://huggingface.co";
  window.parent.postMessage({
    queryString: "".concat(queryArg, "=").concat(elementId)
  }, parentOrigin);
}

;// ./src/index.js
// import { plotClusters } from './clusters'


document.addEventListener("DOMContentLoaded", function () {
  console.log("DOMContentLoaded");
  loadFragments();
  init_memory_plot();
  syncHFSpacesURLHash();
}, {
  once: true
});
/******/ })()
;
//# sourceMappingURL=main.bundle.js.map