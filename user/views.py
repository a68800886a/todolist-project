from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def user_login(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(username, password)
        user = authenticate(request, username=username, password=password)
        if not user:
            message = "帳號或密碼錯誤"
        else:
            login(request, user)
            message = "登陸成功"
            return redirect("todolist")

    return render(request, "user/login.html", {"message": message})


# Create your views here.
def user_resgister(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        print(username, password1, password2)
        if password1 != password2:
            message = "兩次密碼不同!"
        elif len(password1) < 8:
            message = "密碼長度不可小於8"
        else:
            # 使用者名稱是否存在
            user = User.objects.filter(username=username)
            if user:
                message = "使用者名稱已經存在!"
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                message = f"{username},{password1},註冊成功!"

    form = UserCreationForm()
    return render(request, "user/resgister.html", {"form": form, "message": message})
