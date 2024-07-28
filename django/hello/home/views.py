from django.shortcuts import render, HttpResponse


def index(request):
    # return HttpResponse("this is home page!!")
    return render(request ,"index.html" )
def about(request):
    return HttpResponse("This is about page!!")

def services(request):
    return HttpResponse("This is Services page!!")

def contact(request):
    return HttpResponse("This is contact page!!")