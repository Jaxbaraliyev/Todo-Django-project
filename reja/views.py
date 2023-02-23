from django.shortcuts import render, redirect
from django.views import View

from .models import *
from django.contrib.auth import authenticate, login, logout

def home(request):
    if request.method == "POST":
        Reja.objects.create(
            title=request.POST.get('t'),
            description=request.POST['d'],
            status=request.POST['s'],
            vaqt=request.POST['d'],
            student=Student.objects.get(user=request.user)
        )
        return redirect('todo')
    if request.user.is_authenticated:
        st = Student.objects.get(user=request.user)
        r = Reja.objects.filter(student=st)
        data = {
                "rejalar":r,
            }
        return render(request, "todo.html", data)
    else:
        return redirect('login')



def reja_ochir(request, pk):
    Reja.objects.filter(id=pk).delete()
    return redirect("todo")

def reja_edit(request, pk):
    if request.method == 'POST':
        Reja.objects.filter(id=pk).update(
            title=request.POST.get('t'),
            description=request.POST['d'],
            status=request.POST['s'],
            vaqt=request.POST['d']
        )
        return redirect('home')
    data = {
          "reja":Reja.objects.filter(id=pk)
    }
    return render(request, "todo_edit.html", data)


def loginView(request):
    if request.method == "POST":
        users = authenticate(username=request.POST['l'],
                             password=request.POST['p'])
        if users is None:
            return redirect('login')
        login(request, users)
        return redirect('todo')
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect('login')


class RegisterView(View):
    def get(self, request):
        return render(request, 'reg.html')



    def post(self, request):
        u = User.objects.create_user(
            username=request.POST['l'],
            password=request.POST['p']
        )

        Student.objects.create(
            ism=request.POST['i'],
            guruh=request.POST['g'],
            user=u
        )
        return redirect('login')