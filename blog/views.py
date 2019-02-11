from django.http import HttpResponse
from django.shortcuts import render


def hello_times(request, times):
    message = "안녕하세요" * times
    return HttpResponse(message)
