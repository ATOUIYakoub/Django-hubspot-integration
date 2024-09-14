from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from analytics.views import get_hubspot_leads

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('analytics.urls')),  # Include your app's URLs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs', SpectacularSwaggerView.as_view(url_name='schema')),
    path('api/hubspot/leads/', get_hubspot_leads, name='get_hubspot_leads'),
]