// Generated by CoffeeScript 1.8.0
(function() {
  (function($, w) {
    var Addr;
    Addr = (function() {
      var cur_city, cur_district;
      cur_district = 0;
      cur_city = 0;
      return {
        setCity: function(i) {
          return cur_city = i;
        },
        setDistrict: function(i) {
          return cur_district = i;
        },
        getCity: function() {
          return cur_city;
        },
        getDistrict: function() {
          return cur_district;
        }
      };
    })();
    return (function() {
      var blockCount, blockHeight, chooseCity, chooseDistrict, swipe_city, swipe_district;
      chooseCity = function(index, elem, refresh) {
        if (refresh == null) {
          refresh = true;
        }
        Addr.setCity(index);
        $('#ec-addr-city-list .swipe-wrap dd').removeClass('active').eq(index).addClass('active');
        if (refresh) {
          Addr.setDistrict(0);
          return pushDistrict();
        }
      };
      chooseDistrict = function(index, elem, refresh) {
        if (refresh == null) {
          refresh = true;
        }
        $('#ec-addr-district-list .swipe-wrap dd').removeClass('active').eq(index).addClass('active');
        return Addr.setDistrict(index);
      };
      blockHeight = 100;
      blockCount = 5;
      swipe_city = new Swipe(document.getElementById('hc-ill-type'), {
        startSlide: 0,
        disableScroll: false,
        stopPropagation: false,
        transitionEnd: function(index, elem) {
          return null;
        },
        blockHeight: blockHeight,
        blockCount: blockCount
      });
      return swipe_district = new Swipe(document.getElementById('hc-ill-sub'), {
        startSlide: 0,
        disableScroll: false,
        stopPropagation: false,
        transitionEnd: function(index, elem) {
          return null;
        },
        blockHeight: blockHeight,
        blockCount: blockCount
      });
    })();
  })(Zepto, window);

}).call(this);
