from django.conf.urls import url, include
from django.contrib import admin
from django.views import static

from .settings import MEDIA_ROOT
import accounts.urls
import cart.urls
import checkout.urls
from products.views import products_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', products_list, name='index'),
    url(r'^search/$', products_list, name='search'),  # handled by same view as index page
    url(r'^accounts/', include(accounts.urls)),
    url(r'^cart/', include(cart.urls)),
    url(r'^checkout/', include(checkout.urls)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
