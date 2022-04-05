from django.contrib import admin
from django.urls import path, include

from config import settings

urlpatterns = [
    # MAIN URLS
    path('controlme/', admin.site.urls),
    path('', include('mainsite.urls')),
    path('profiller/', include('profiles.urls')),

    # ADDITIONAL URLS
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    # path('manifest.json', TemplateView.as_view(template_name="manifest.json", content_type='application/json')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
