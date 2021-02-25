from django.contrib import admin
from django.http import HttpResponse, HttpRequest
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from main.handlers.index import handler_django
from tasks.lesson01 import task103
from tasks.lesson03 import task301, task302, task303, task304, task305, task306, task307, task309, task310, task311
from tasks.lesson04 import task402


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
    path("", handler_django),
    path("tasks/lesson01/task103.html/", task103.handler),
    path("tasks/lesson03/task301.html/", task301.handler),
    path("tasks/lesson03/task302.html/", task302.handler),
    path("tasks/lesson03/task303.html/", task303.handler),
    path("tasks/lesson03/task304.html/", task304.handler),
    path("tasks/lesson03/task305.html/", task305.handler),
    path("tasks/lesson03/task306.html/", task306.handler),
    path("tasks/lesson03/task307.html/", task307.handler),
    path("tasks/lesson03/task309.html/", task309.handler),
    path("tasks/lesson03/task310.html/", task310.handler),
    path("tasks/lesson03/task311.html/", task311.handler),
    path("api/v1/tasks/402/", task402.handler_api,
    path("tasks/lesson04/task402.html/", csrf_exempt(task402.handler))
]

