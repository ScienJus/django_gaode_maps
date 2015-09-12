$(document).ready(function() {
    var location = ($("#id_location").val() && $("#id_location").val().split(",")) || [116.397428, 39.90923];
    //实例化地图
    var map = new AMap.Map("mapContainer", {
        center: location,
        resizeEnable: true,
        zoom: 13
    });
    //实例化标记
    var marker = new AMap.Marker({
        position: location,
        map:map
    });

    //实例化坐标转换地址
    var geocoder;
    AMap.service('AMap.Geocoder',function(){
        geocoder = new AMap.Geocoder({});
    })

    //注册地图的click事件
    var clickEventListener = map.on( 'click', function(e) {
        var location = [e.lnglat.getLng(), e.lnglat.getLat()];
        //设置坐标
        $("#id_location").val(location.join(","));
        //得到城市
        map.getCity(function (data) {
            if (data['province'] && typeof data['province'] === 'string') {
                $("#id_city").val(data['city'] || data['province']);
            }
        });
        //得到地址
        geocoder.getAddress(e.lnglat, function(status, result) {
            if (status === 'complete' && result.info === 'OK') {
               $("#id_address").val( result.regeocode.formattedAddress);
               $("#id_postal_code").val( result.regeocode.addressComponent.adcode);
            }
        });
        //更新中心点
        map.setCenter(location);
        //更新标记
        marker.setPosition(location);
    });
});