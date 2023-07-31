from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    # http://127.0.0.1:8000/

    return HttpResponse("Hello, world. Demoapp.")


def drinks(request, drink):
    # http://127.0.0.1:8000/drinks/orange

    return HttpResponse(f'My drinks is {drink}.')


def httpObject(request):
    # http://127.0.0.1:8000/http/

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


def query(req):
    # http://127.0.0.1:8000/query/?name=john&id=2
    
    name = req.GET['name']
    id = req.GET['id']
    return HttpResponse(f'Name: {name}, UserID:{id}')
