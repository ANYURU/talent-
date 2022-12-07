from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey, this is the first version of my api.")