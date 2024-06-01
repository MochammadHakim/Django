from django.contrib import admin
from django.urls import path, include
from library import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.loginadm, name='loginadm'),
    path('input/', views.input, name='input'),
    path('buku/<int:pk>/', views.detailbook, name='detailbook'),
    path('logout/', views.logoutadm, name="logout"),
    path('', include('library.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
