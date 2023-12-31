from demoapp.forms import InputForm, LogForm
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

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


def showForm(request):
    # http://127.0.0.1:8000/showForm/

    return render(request, "form.html")


def getForm(request):
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
    return HttpResponse("Name:{} UserID:{}".format(name, id))


def myReverse(request):
    rev = reverse("demoapp:myReverse")
    return HttpResponse(f'Path: {rev}')


def formInputForm(request):
    form = InputForm()
    context = {"form": form}
    return render(request, "home.html", context)


def formLogForm(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "home.html", context)


def home1(request):
    return render(request, "home1.html", {})


def register(request):
    return render(request, "register.html", {})


def login(request):
    return render(request, "login.html", {})
