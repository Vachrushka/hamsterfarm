from django.urls import path, include
from rest_framework import routers
from .viewsets import *

router = routers.DefaultRouter()
router.register('tg-enter', GetScriptViewSet, basename='tg-enter')
router.register('tg-enter-filtered', GetScriptWindViewSet, basename='tg-enter-filtered')
router.register('clicker', GetClickerViewSet, basename='clicker')


urlpatterns = [
    path('', include(router.urls)),
]
