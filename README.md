# Django Gaode Maps

参考[django_google_maps][1]自己随便写的一个Django管理后台的高德地图控件。

###如何使用

1. 在`settings.py`中的`INSTALLED_APPS`加入`django_gaode_maps`
2. 在该文件中定义`GAODE_MAPS_KEY`的值为你使用高德地图api的key
3. 在`models.py`中定义你的model，可以使用的属性名有`address`、`location`和`city`，分别对应着地图上点所在位置的地址、坐标（lng,lat）和城市。
4. 最好使用这三个名称作为model的属性名，你可以通过`db_column`属性映射数据库中对应的字段，如果实在无法做到则需要在`form`中定义表单项的id为`id_address`、`id_location`和`id_city`。
5. 使用与属性对应的字段类`AddressField`、`LocationField`和`CityField`。
6. 在`admin.py`中通过`formfield_overrides`的属性将你使用到的一个字段类映射为`GaodeMapsWidget`（只需要映射一个字段类即可）。

接下来便可以在管理界面中看到高德地图的控件了，效果大概是这样的：

![效果][2]

[1]:https://github.com/madisona/django-google-maps
[2]:http://www.scienjus.com/wp-content/uploads/2015/09/QQ图片20150912234103.png
