from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(requst):
    result = {"message": "測試", "data": 123, "label": "文字標籤"}
    return HttpResponse(result)
