from rest_framework import routers

from .views import SectionViewSet, BlockViewSet

# Routers provide an easy way of automatically determining the URL conf.
# These are the Django Rest available routes
router = routers.DefaultRouter()
router.register(r'sections', SectionViewSet)
router.register(r'block', BlockViewSet)
# router.register(r'block', BlockViewSet)
