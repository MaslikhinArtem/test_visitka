from django.shortcuts import render, redirect
from django.template.context_processors import request
from .forms import ReviewForm

def index(request):
    return render(request, 'main/index.html')
def about(request):
    return render(request, 'main/about.html')
def forum(request):
    return render(request, 'main/forum.html')
def form(request):
    error = ''
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "*форма заполнена неверно"
    form = ReviewForm()
    data = {
        'form':form,
        "error": error,
    }
    return render(request, 'main/form.html', data)

def bk_vilka(request):
    return render(request, 'main/bk_vilka.html')
