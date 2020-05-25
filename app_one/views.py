from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.middleware import csrf
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import requires_csrf_token


def result(request):
    if request.method == 'POST':
        strToReturn = ("full Name: " + request.POST['fullName'] +
                            " <br/>Dojo location: " + request.POST['dojoLocation'] +
                            "<br/>favorite Language: " + request.POST['favoriteLanguage'])
        try:
            strToReturn = strToReturn + "<br/>Comment: " + request.POST["comment"]
        except:
            print("no comment added")
        return HttpResponse(strToReturn)
    else:
        return redirect('/')

@requires_csrf_token
def index(request):
    return render(request, "index.html")
    # return HttpResponse(myHtml)
