from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from schooler import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.home, name='home'),
    path('school/', include('school.urls')),  # Include the URLs from the school app
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
