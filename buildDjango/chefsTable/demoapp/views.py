from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return HttpResponse("Hello, world. Demoapp.")


def drinks(request, drink):
    return HttpResponse(f'My drinks is {drink}.')


def httpDemo(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    userAgent = request.META['HTTP_USER_AGENT']
    pathInfo = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 20

    message = f"""
    <br>Path:               {path}
    <br>Address:            {address}
    <br>Scheme:             {scheme}
    <br>Method:             {method}
    <br>User agent:         {userAgent}
    <br>Path info:          {pathInfo}
    <br>Response header:    {response.headers}
    """
    return HttpResponse(message, content_type='text/html', charset='utf-8')
