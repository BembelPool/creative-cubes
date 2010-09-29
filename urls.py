from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

import settings

urlpatterns = patterns('',
	(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT } ),
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('cms.urls')),
)