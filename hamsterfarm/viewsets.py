from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

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

class GetScriptWindViewSet(viewsets.GenericViewSet):
    filter_backends = [DjangoFilterBackend]
    def list(self, request):
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
