from django.shortcuts import render, redirect

# Create your views here.
from .forms import NewUserForm
from .models import User

def index(request):
    allusers=User.objects.all()
    return render(request, 'App/index.html', {'user_list': allusers})

def users(request):
    new_form = NewUserForm(request.POST or None)
    if new_form.is_valid():
        new_form.save()
        return redirect('index')
    return render(request, 'App/users.html', {'userform': new_form})

def createuser(request, id):
    user = get_object_or_404(User, pk=id)
    read_form = NewUserForm(request.POST or None, instance=user)
    if read_form.is_valid():
        read_form.save()
        return redirect('index')
    return render(request, 'm_f_app/users.html', {'userform': read_form})

def readuser(request, id):
    user = get_object_or_404(User, pk=id)
    read_form = NewUserForm(request.POST or None, instance=user)
    if read_form.is_valid():
        read_form.save()
        return redirect('index')
    return render(request, 'm_f_app/users.html', {'userform': read_form})

def updateuser(request, id):
    user = get_object_or_404(User, pk=id)
    update_form = NewUserForm(request.POST or None, instance=user)
    if update_form.is_valid():
        update_form.save()
        return redirect('index')
    return render(request, 'm_f_app/users.html', {'userform': update_form})

def deleteuser(request, id):
    user = get_object_or_404(User, pk=id)
    delete_form = NewUserForm(request.POST or None, instance=user)
    if delete_form.is_valid():
        delete_form.save()
        return redirect('index')
    return render(request, 'm_f_app/users.html', {'userform': delete_form})
