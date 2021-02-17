from django.contrib import admin
from django.http import HttpResponse, HttpRequest
from django.urls import path



def xxxx(req):

    number = req.GET.get("number")
    if number:
        req.session["number"] = number
    else:
        number = req.session.get("number")

    return HttpResponse(f"hello world! method: {req.method}"
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", xxxx),
]

