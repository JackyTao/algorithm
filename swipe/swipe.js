(function() {
  window.Swipe = function(container, options) {
    "use strict";
    var browser, circle, delta, element, events, index, length, move, noop, offloadFn, setup, slidePos, slides, speed, start, translate, width;
    noop = function() {};
    offloadFn = function(fn) {
      return setTimeout(fn || noop, 0);
    };
    browser = {
      addEventListener: !!window.addEventListener,
      touch: ('ontouchstart' in window) || window.DocumentTouch && document instanceof DocumentTouch,
      transitions: (function(temp) {
        var i, props, r, _i, _len;
        props = ['transitionProperty', 'WebkitTransition', 'MozTransition', 'OTransition', 'msTransition'];
        r = false;
        for (_i = 0, _len = props.length; _i < _len; _i++) {
          i = props[_i];
          r = r || (temp.style[i] !== void 0);
        }
        return r;
      })(document.createElement('swipe'))
    };
    if (!container) {
      return;
    }
    element = container.children[0];
    options || (options = {});
    index = 0;
    speed = options.speed || 300;
    slidePos = slides = width = length = null;
    setup = function() {
      var c, i, pos, slide;
      slidePos = null;
      index = options.startSlide;
      slides = (function() {
        var _i, _len, _ref, _results;
        _ref = element.children;
        _results = [];
        for (i = _i = 0, _len = _ref.length; _i < _len; i = ++_i) {
          c = _ref[i];
          if (i < options.blockCount) {
            _results.push(c);
          }
        }
        return _results;
      })();
      length = slides.length;
      slidePos = new Array(slides.length);
      width = options.blockHeight;
      element.style.height = options.blockCount * options.blockHeight + 'px';
      pos = slides.length;
      while (pos--) {
        slide = slides[pos];
        slide.style.height = "" + width + "px";
        slide.setAttribute('data-index', pos);
        if (browser.transitions) {
          slide.style.top = (pos * -width) + 'px';
          move(pos, pos * width, 0);
        }
      }
      if (!browser.transitions) {
        element.style.top = (index * -width) + 'px';
      }
      return container.style.visibility = 'visible';
    };
    circle = function(index) {
      return (slides.length + (index % slides.length)) % slides.length;
    };
    move = function(index, dist, speed) {
      translate(index, dist, speed);
      return slidePos[index] = dist;
    };
    translate = function(index, dist, speed) {
      var slide, style;
      slide = slides[index];
      style = slide && slide.style;
      if (!style) {
        return;
      }
      style.webkitTransitionDuration = style.MozTransitionDuration = style.msTransitionDuration = style.OTransitionDuration = style.transitionDuration = speed + 'ms';
      style.webkitTransform = 'translate(0,' + dist + 'px)' + 'translateZ(0)';
      return style.msTransform = style.MozTransform = style.OTransform = 'translateY(' + dist + 'px)';
    };
    start = {};
    delta = {};
    events = {
      handleEvent: function(event) {
        switch (event.type) {
          case 'touchstart':
            return this.start(event);
          case 'touchmove':
            return this.move(event);
          case 'touchend':
            return offloadFn(this.end(event));
          case 'webkitTransitionEnd':
          case 'msTransitionEnd':
          case 'oTransitionEnd':
          case 'otransitionend':
          case 'transitionend':
            return offloadFn(this.transitionEnd(event));
          case 'resize':
            return offloadFn(setup);
        }
      },
      start: function(event) {
        var touches;
        touches = event.touches[0];
        start = {
          x: touches.pageX,
          y: touches.pageY,
          time: +(new Date)
        };
        delta = {};
        element.addEventListener('touchmove', this, false);
        return element.addEventListener('touchend', this, false);
      },
      move: function(event) {
        var diff, i, touches, v, _i, _len, _results;
        if (event.touches.length > 1 || event.scale && event.scale !== 1) {
          return;
        }
        if (options.disableScroll) {
          event.preventDefault();
        }
        touches = event.touches[0];
        delta = {
          x: touches.pageX - start.x,
          y: touches.pageY - start.y
        };
        event.preventDefault();
        if (delta.y > 0) {
          if (Math.abs(delta.y) > index * width) {
            diff = delta.y - index * width;
            delta.y = index * width + diff / (diff / width + 5);
          }
        } else {
          if (Math.abs(delta.y) > (slides.length - index - 1) * width) {
            diff = Math.abs(delta.y) - (slides.length - index - 1) * width;
            delta.y = -((slides.length - index - 1) * width + diff / (diff / width + 5));
          }
        }
        _results = [];
        for (i = _i = 0, _len = slidePos.length; _i < _len; i = ++_i) {
          v = slidePos[i];
          _results.push(translate(i, delta.y + v, 0));
        }
        return _results;
      },
      end: function(event) {
        var direction, duration, eleCount, i, isPastBounds, isValidSlide, v, _i, _j, _k, _len, _len1, _len2;
        duration = +(new Date) - start.time;
        isValidSlide = Number(duration) < 250 && Math.abs(delta.y) > 20 || Math.abs(delta.y) > width / 2;
        eleCount = Math.ceil(Math.floor(Math.abs(delta.y) / width * 2) / 2);
        isPastBounds = !index && delta.y > 0 || index === slides.length - 1 && delta.y < 0;
        direction = delta.y < 0;
        if (isValidSlide && !isPastBounds) {
          if (direction) {
            for (i = _i = 0, _len = slidePos.length; _i < _len; i = ++_i) {
              v = slidePos[i];
              move(i, -eleCount * width + v, 0);
            }
            index = circle(index + eleCount);
          } else {
            for (i = _j = 0, _len1 = slidePos.length; _j < _len1; i = ++_j) {
              v = slidePos[i];
              move(i, eleCount * width + v, 0);
            }
            index = circle(index - eleCount);
          }
          options.callback && options.callback(index, slides[index]);
        } else {
          for (i = _k = 0, _len2 = slidePos.length; _k < _len2; i = ++_k) {
            v = slidePos[i];
            move(i, v, 0);
          }
        }
        element.removeEventListener('touchmove', events, false);
        return element.removeEventListener('touchend', events, false);
      },
      transitionEnd: function(event) {
        if (parseInt(event.target.getAttribute('data-index'), 10) === index) {
          return options.transitionEnd && options.transitionEnd.call(event, index, slides[index]);
        }
      }
    };
    setup();
    if (browser.addEventListener) {
      if (browser.touch) {
        element.addEventListener('touchstart', events, false);
      }
      if (browser.transitions) {
        element.addEventListener('webkitTransitionEnd', events, false);
        element.addEventListener('msTransitionEnd', events, false);
        element.addEventListener('oTransitionEnd', events, false);
        element.addEventListener('otransitionend', events, false);
        element.addEventListener('transitionend', events, false);
      }
      window.addEventListener('resize', events, false);
    } else {
      window.onresize = function() {
        return setup();
      };
    }
    return {
      refresh: function(blockCount, startSlide, needCallback) {
        var i, v, _i, _len;
        if (needCallback == null) {
          needCallback = true;
        }
        options.blockCount = blockCount;
        setup();
        for (i = _i = 0, _len = slidePos.length; _i < _len; i = ++_i) {
          v = slidePos[i];
          move(i, -startSlide * width + v, 0);
        }
        index = circle(startSlide);
        if (needCallback) {
          return options.callback && options.callback(index, slides[index]);
        }
      },
      kill: function() {
        var pos, slide;
        element.style.width = '';
        element.style.left = '';
        pos = slides.length;
        while (pos--) {
          slide = slides[pos];
          slide.style.width = '';
          slide.style.left = '';
          if (browser.transitions) {
            translate(pos, 0, 0);
          }
        }
        if (browser.addEventListener) {
          element.removeEventListener('touchstart', events, false);
          element.removeEventListener('webkitTransitionEnd', events, false);
          element.removeEventListener('msTransitionEnd', events, false);
          element.removeEventListener('oTransitionEnd', events, false);
          element.removeEventListener('otransitionend', events, false);
          element.removeEventListener('transitionend', events, false);
          return window.removeEventListener('resize', events, false);
        } else {
          return window.onresize = null;
        }
      }
    };
  };

}).call(this);
