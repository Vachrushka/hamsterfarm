from django.urls import path, include
from rest_framework import routers
from .viewsets import *

router = routers.DefaultRouter()
router.register('tg-enter', GetEnterViewSet, basename='tg-enter')
router.register('tg-enter-new-wind', GetEnterNewWindViewSet, basename='tg-enter-new-wind')
router.register('clicker', GetClickerViewSet, basename='clicker')
router.register('clicker-new-wind', GetClickerNewWindViewSet, basename='clicker-new-wind')


urlpatterns = [
    path('', include(router.urls)),
]
