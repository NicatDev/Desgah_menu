from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
# from marketapp.sitemap import BlogSiteMap,ServiceSitemap, StaticSitemap
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns
from menu.sitemap import *

sitemaps = {
    'static_sitemap': StaticSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('menu.urls')),
    path('robots.txt/', TemplateView.as_view(template_name='robots.txt', content_type="text/plain")),
    path(
        'sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'
    ),
]


urlpatterns += static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)