from django.http import HttpResponse
from django.shortcuts import render

def week3_assignment(request):
    return render(request, 'week3/base.html', {})