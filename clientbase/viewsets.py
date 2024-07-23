from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .scripts import *


def check_token_status(request, access):
    return True
    token_value = request.query_params.get('token', '')
    token = Token.objects.filter(token=token_value).first()

    if token and token.access.filter(name=access).exists():
        return True
    return False


class GetEnterViewSet(viewsets.GenericViewSet):
    filter_backends = [DjangoFilterBackend]

    @extend_schema(
        parameters=[
            OpenApiParameter(name='token', description='token', required=True,
                             type=str)
        ]
    )
    def list(self, request):
        if check_token_status(request, access='enter'):
            return Response(get_access_enter(), status=status.HTTP_200_OK)
        return Response(status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)


class GetEnterNewWindViewSet(viewsets.GenericViewSet):
    filter_backends = [DjangoFilterBackend]

    @extend_schema(
        parameters=[
            OpenApiParameter(name='new_tab', description='Is in new tab?', type=str, default='true'),
            OpenApiParameter(name='token', description='token', required=True,
                             type=str)
        ]
    )
    def list(self, request):
        if check_token_status(request, access='enter-new-window'):
            new_tab = request.query_params.get('new_tab')
            if new_tab is not None:
                new_tab = 'true' if new_tab.lower() in ['true', '1', 't'] else 'false'
            else:
                new_tab = 'false'
            return Response(get_access_new_wind(new_tab), status=status.HTTP_200_OK)
        return Response(status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)


class GetClickerViewSet(viewsets.GenericViewSet):
    filter_backends = [DjangoFilterBackend]

    @extend_schema(
        parameters=[
            OpenApiParameter(name='token', description='token', required=True, type=str)
        ]
    )
    def list(self, request):
        if check_token_status(request, access='clicker'):
            script = get_access_click()
            return Response(script, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)


class GetClickerNewWindViewSet(viewsets.GenericViewSet):
    filter_backends = [DjangoFilterBackend]

    @extend_schema(
        parameters=[
            OpenApiParameter(name='new_tab', description='Is in new tab?', type=str, default='true'),
            OpenApiParameter(name='token', description='token', required=True,
                             type=str)
        ]
    )
    def list(self, request):
        if check_token_status(request, access='clicker-new-window'):
            new_tab = request.query_params.get('new_tab')
            if new_tab is not None:
                new_tab = 'true' if new_tab.lower() in ['true', '1', 't'] else 'false'
            else:
                new_tab = 'false'
            script = get_access_click_new_web(new_tab)
            return Response(script, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)
