from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from drf_spectacular.utils import extend_schema, OpenApiParameter

def check_token_status(request, access):
    token_value = request.query_params.get('token','')
    token = Token.objects.filter(token=token_value).first()

    if token and token.access.filter(name=access).exists():
        return True
    return False

class GetScriptViewSet(viewsets.GenericViewSet):
    filter_backends = [DjangoFilterBackend]

    @extend_schema(
        parameters=[
            OpenApiParameter(name='token', description='token', required=True,
                             type=str)
        ]
    )
    def list(self, request):
        if check_token_status(request, access='enter'):
            script = ("if (location.hostname === 'hamsterkombatgame.io') {"
                      "const original_indexOf = Array.prototype.indexOf;"
                      "Array.prototype.indexOf = function (...args) {"
                      "if (JSON.stringify(this) === JSON.stringify(['android', 'android_x', 'ios'])) {"
                      "setTimeout(() => {Array.prototype.indexOf = original_indexOf;}, 0);"
                      "return 0; }"
                      "return original_indexOf.apply(this, args);};}")
            return Response(script, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)

class GetScriptWindViewSet(viewsets.GenericViewSet):
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

            script = ("if (location.hostname === 'hamsterkombatgame.io') {"
                      "const original_indexOf = Array.prototype.indexOf;"
                      "Array.prototype.indexOf = function (...args) {"
                      "if (JSON.stringify(this) === JSON.stringify(['android', 'android_x', 'ios'])) {"
                      "setTimeout(() => {"
                      "Array.prototype.indexOf = original_indexOf;});"
                      "return 0;}"
                      "return original_indexOf.apply(this, args);};"
                      f"if ({new_tab}) "
                      "{const iframe = document.querySelector('iframe');"
                      "const web_link = document.URL;"
                      "if (confirm('Открыть хомяка в отдельном окне?')) {"
                      "window.open(web_link, '_blank');}}}")
            return Response(script, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)

class GetClickerViewSet(viewsets.GenericViewSet):
    filter_backends = [DjangoFilterBackend]
    @extend_schema(
        parameters=[
            OpenApiParameter(name='token', description='token', required=True,
                             type=str)
        ]
    )
    def list(self, request):
        if check_token_status(request, access='clicker-new-window'):
            script = ("if (location.hostname === 'hamsterkombatgame.io') {oldSubstring = '=web&';"
                      "newSubstring = '=android&';const web_link = document.URL;"
                      "let newWebLink = web_link.replace(oldSubstring, newSubstring);window.open(newWebLink);"
                      "const buttonSelector = '.user-tap-button';"
                      "const energySelector = '.user-tap-energy > p';"
                      "let reachedZeroEnergy = false;"
                      "let button;let attempts = 0;const maxAttempts = 100;"
                      "function checkButtonAndEnergy() {attempts++;"
                      "button = document.querySelector(buttonSelector);"
                      "if (button || attempts >= maxAttempts) {"
                      "if (button) {"
                      "console.log('Button found');"
                      "} else {console.log('Max attempts reached, stopping search');}"
                      "clearInterval(searchInterval);"
                      "tick();} else {"
                      "console.log('Button not found yet, attempt:', attempts);}}"
                      "function tick() {try {const energyElement = document.querySelector(energySelector);"
                      "if (energyElement) {const energyStr = energyElement.innerText;"
                      "const [currEnergy, maxEnergy] = energyStr.split('/').map(Number);if (!reachedZeroEnergy) {"
                      "button.dispatchEvent(new PointerEvent('pointerup'));"
                      "button.dispatchEvent(new PointerEvent('pointerup'));"
                      "button.dispatchEvent(new PointerEvent('pointerup'));"
                      "button.dispatchEvent(new PointerEvent('pointerup'));}"
                      "if (currEnergy <= 10) {reachedZeroEnergy = true;}"
                      "if (currEnergy >= maxEnergy - 10) {"
                      "reachedZeroEnergy = false;}}} catch (e) {console.log(e);}setTimeout(tick, 100 * Math.random() + 50);}"
                      "const searchInterval = setInterval(checkButtonAndEnergy, 500);}")

            return Response(script, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS)