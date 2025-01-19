from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .form import UerBioForm, UserSendFile
from random import random
from django.views.decorators.cache import cache_page


def index(request):
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    res = a + b
    context = {'a': a,
               'b': b,
               'res': res,
               }
    return render(request, 'requestdataapp/rqp.html', context=context)


def bio_user(request):
    context = {
        'form': UerBioForm()
    }
    return render(request, 'requestdataapp/ubf.html', context=context)


def hzwat(request):
    if request.method == 'POST':
        form = UserSendFile(request.POST, request.FILES)
        if form.is_valid():
            myfile = form.cleaned_data['file']
            fs = FileSystemStorage()
            ok = fs.save(myfile.name, myfile)
            print('ALL  ACCAPTE', ok)
    else:
        form = UserSendFile()
    context = {
        'mainn': form,
    }
    return render(request, 'requestdataapp/upus.html', context=context)

@cache_page(timeout=30)
def main(request):
    c = {
        'o': random(),
    }
    return render(request, 'requestdataapp/main.html', context=c)
