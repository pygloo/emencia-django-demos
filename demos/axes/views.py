# django import
from django.http import HttpResponse
from django.template import RequestContext, loader
# axes import
from axes.decorators import staff_member_required

def index(request):
    # get template
    _template = loader.get_template("axes/index.html")
    # render
    return HttpResponse(_template.render(RequestContext(request, {})))
# axes use
index = staff_member_required(index)
