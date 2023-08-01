from django.http import HttpResponse, HttpResponseNotFound


def handler404(request, exception):
    # HttpResponse is more general, 
    # HttpResponseNotFound make exception more specific
    return HttpResponseNotFound("my404: Page not found.")
