from django.urls import path, include
from rest_framework import routers
from .viewsets import *
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register('tg-enter', GetScriptViewSet, basename='tg-enter')

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]
