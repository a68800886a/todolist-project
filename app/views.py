from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random


def lotto(request):
    numbers = random.sample(range(1, 50), 6)
    numbers = sorted(numbers)
    numbers = "".join(map(str, numbers))

    spec_number = random.randint(1, 49)

    result = {"numbers": numbers, "spec_number": spec_number}

    return render(request, "lotto.html", result)


# Create your views here.
def hello(request):
    result = {"message": "測試", "data": 123, "label": "文字標籤"}
    return HttpResponse(result)
