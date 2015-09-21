(($, w) ->
    Addr = (->

        cur_district = 0
        cur_city = 0


        setCity: (i) -> cur_city = i
        setDistrict: (i) -> cur_district = i

        getCity: -> cur_city
        getDistrict: -> cur_district
    )()
    (->
        chooseCity = (index, elem, refresh=true) ->
            Addr.setCity index
            $('#ec-addr-city-list .swipe-wrap dd')
            .removeClass 'active'
            .eq(index).addClass 'active'
            if refresh
                Addr.setDistrict 0
                pushDistrict()
        chooseDistrict = (index, elem, refresh=true) ->
            $('#ec-addr-district-list .swipe-wrap dd')
            .removeClass 'active'
            .eq(index).addClass 'active'
            Addr.setDistrict index

        blockHeight = 100
        blockCount = 5
        #$('.swipe-wrap').css('top', 2 + 2 * blockHeight + 'px')


        swipe_city = new Swipe(document.getElementById('hc-ill-type'), {
            startSlide: 0,
            disableScroll: false,
            stopPropagation: false,
            #callback: chooseCity,
            transitionEnd: (index, elem) -> null,
            blockHeight: blockHeight,
            blockCount: blockCount,
        })

        swipe_district = new Swipe(document.getElementById('hc-ill-sub'), {
            startSlide: 0,
            disableScroll: false,
            stopPropagation: false,
            #callback: chooseDistrict,
            transitionEnd: (index, elem) -> null,
            blockHeight: blockHeight,
            blockCount: blockCount,
        })


        #pushCity = ->
        #    tts = Addr.addr_tree()
        #    cities = tts[Addr.getProvince()].children

        #    eles = $('#ec-addr-city-list .swipe-wrap dd')
        #    eles.html ''
        #    $(eles[i]).html addr.name for addr, i in cities
        #    swipe_city.refresh cities.length, Addr.getCity()


        #pushDistrict = ->
        #    tts = Addr.addr_tree()
        #    districts = tts[Addr.getProvince()].children[Addr.getCity()].children

        #    eles = $('#ec-addr-district-list .swipe-wrap dd').html ''
        #    $(eles[i]).html addr.name for addr, i in districts
        #    swipe_district.refresh districts.length, Addr.getDistrict()

        #initAddr = ->
        #    # input init addr
        #    $('#ec-addr-full-district').html Addr.getFullAddr()
        #    $('#ec-addr-area-id').val Addr.getAreaId()
        #    refreshAddrView()
        #    
        #refreshAddrView = ->
        #    tts = Addr.addr_tree()

        #    cities = tts[Addr.getProvince()].children

        #    cityDom = $('#ec-addr-city-list .swipe-wrap dd').html ''
        #    $(cityDom[i]).html addr.name for addr, i in cities
        #    swipe_city.refresh cities.length, Addr.getCity(), false
        #    chooseCity Addr.getCity(), null, false

        #    districts = tts[Addr.getProvince()].children[Addr.getCity()].children

        #    districtDom = $('#ec-addr-district-list .swipe-wrap dd').html ''
        #    $(districtDom[i]).html addr.name for addr, i in districts
        #    swipe_district.refresh districts.length, Addr.getDistrict(), false
        #    chooseDistrict Addr.getDistrict(), null, false
    )()
)(Zepto, window)
