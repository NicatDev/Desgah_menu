from django.contrib.sitemaps import Sitemap
from menu.models import *
from django.urls import reverse, NoReverseMatch

class StaticSitemap(Sitemap):
    protocol = 'https'
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return [
            'home'
        ]

    def location(self, item):
        try:
            return reverse(item)
        except NoReverseMatch:
            return reverse('home')