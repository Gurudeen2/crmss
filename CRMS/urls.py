from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('pages.urls')),
    path('crime/', include('crime.urls')),
    path('criminal/', include('criminal.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
