from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from analytics.views import get_hubspot_leads, post_hubspot_lead_view, update_hubspot_lead_view, delete_hubspot_lead_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('api/hubspot/leads/', get_hubspot_leads, name='get_hubspot_leads'),
    path('api/hubspot/leads/post/', post_hubspot_lead_view, name='post_hubspot_lead'),
    path('api/hubspot/leads/<int:pk>/', update_hubspot_lead_view, name='update_hubspot_lead'),
    path('api/hubspot/leads/<int:pk>/delete/', delete_hubspot_lead_view, name='delete_hubspot_lead'),
]