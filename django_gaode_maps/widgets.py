from django.forms.widgets import *
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt
from django.conf import settings

class LocationWidget(TextInput):

    class Media:
        css = {'all': ('css/gaode_maps.css',)}
        js = (
            'http://libs.baidu.com/jquery/1.9.1/jquery.min.js',
            'http://webapi.amap.com/maps?v=1.3&key=' + settings.GAODE_MAPS_KEY,
            'js/gaode_maps.js',
        )

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '' and value is not None:
            final_attrs['value'] = self._format_value(value)
        html = u'<input%s /><div id="mapContainer"></div>'
        return mark_safe(html % flatatt(final_attrs))