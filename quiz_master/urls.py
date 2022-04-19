from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin, sitemaps
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz_master.quiz_app.urls')),
    path('accounts/', include('quiz_master.accounts.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
