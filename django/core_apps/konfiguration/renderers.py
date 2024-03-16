import json

from rest_framework.renderers import JSONRenderer


class KonfigurationJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context is None:
            status_code = 200
        else:
            status_code = renderer_context["response"].status_code

        if data is not None:
            errors = data.get("errors", None)
        else:
            errors = None

        if errors is not None:
            return super(KonfigurationJSONRenderer, self).render(data)

        return json.dumps({"status_code": status_code, "modul":"Konfiguration", "data": data})


class KonfigurationenJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code

        errors = data.get("errors", None)

        if errors is not None:
            return super(KonfigurationenJSONRenderer, self).render(data)

        return json.dumps({"status_code": status_code, "modul":"Konfiguration", "data": data})