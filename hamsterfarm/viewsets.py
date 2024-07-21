from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class GetScriptViewSet(viewsets.GenericViewSet):

    def list(self, request):
        script = ("if (location.hostname === 'hamsterkombatgame.io') {"
                  "const original_indexOf = Array.prototype.indexOf;"
                  "Array.prototype.indexOf = function (...args) {"
                  "if (JSON.stringify(this) === JSON.stringify(['android', 'android_x', 'ios'])) {"
                  "setTimeout(() => {Array.prototype.indexOf = original_indexOf;}, 0);"
                  "return 0; }"
                  "return original_indexOf.apply(this, args);};}")
        return Response(script, status=status.HTTP_200_OK)
