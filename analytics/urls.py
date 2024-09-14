from rest_framework.routers import DefaultRouter
from .views import LeadViewSet, InteractionViewSet

router = DefaultRouter()
router.register(r'leads', LeadViewSet)
router.register(r'interactions', InteractionViewSet)

urlpatterns = router.urls
