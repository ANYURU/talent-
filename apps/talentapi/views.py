from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def endpoints(request):
    data = ['users', 'developers', 'recruiters', 'jobs']
    return JsonResponse(data, safe=False)
