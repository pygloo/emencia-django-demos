from django.http import HttpResponse
from django.template import RequestContext, loader

from demos.gmaps.models import GMap

def index(request):
    # get template
    _template = loader.get_template("gmaps/index.html")
    # get the first field
    _field = (GMap.objects.all()\
            and GMap.objects.all()[0])\
            or {"map_field": {show: "No maps defined"}}
    # render field
    return HttpResponse(
            _template.render(
                RequestContext(
                    request,
                    {"field": _field}
                    )
                )
            )
