from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('clone.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('tinymce/', include('tinymce.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
