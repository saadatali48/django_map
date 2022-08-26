from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from apps.appadmin import views as admin_views
from apps.customer.views import SampleMapView
from .api_urls import urlpatterns as api_urlpatterns

urlpatterns = [
    path('', SampleMapView.as_view(), name='sample_map_view'),
    # TemplateView -- input favico
    path('admin/', admin.site.urls),
    path('login/', admin_views.login_user, name='login_user'),
    path('logout/', admin_views.logout_user, name='logout'),
]

urlpatterns += api_urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)