from django.shortcuts import redirect
from django.shortcuts import render
from .forms import UserForm
from .models import User
# Create your views here.
def add(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect("show")

def show(request):
    stud = User.objects.all()
    return render(request, "view.html", {'stu':stud})

def ShowDetailsPage(request):
    form = UserForm(request.POST or None)
    return render(request, "index.html", {'form': form})

def EditPage(request, id):
    data = User.objects.get(id = id)
    return render(request, "edit.html", {'data': data})

def SaveEdit(request):
    data = User.objects.get(id = request.POST['id'])
    form = UserForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
    return redirect("show")


def ConfirmDelete(request, id):
    User.objects.filter(id=id).delete()
    return redirect("show")
