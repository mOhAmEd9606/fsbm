from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, Group, Permission
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from article.models import *

# Create your views here.
from .forms import  *
from etudiant.models import *
from .models import *

def home(request):
    context = {
        'Filiernavebar': Filier.objects.all().order_by('pk'),
        'Article': Article.objects.all().order_by('pk'),
        'Cat': Cat.objects.all().order_by('pk'),
        'Filier': Filier.objects.all(),
        'Module': Module.objects.all(),
        'Modulepop': Module.objects.all().order_by('show')[:5],
        'Semmester': Semmester.objects.all(),
         'lastCours': Cours.objects.all().order_by('-pk')[:5],
         'Cours': Cours.objects.all().order_by('-pk')[:7],
    }
    return render(request,'front/home.html',context)
@login_required(login_url='loginPage')

def panel(request):
    lenEmail = len(Newsletter.objects.filter(status=1))
    lenPhone = len(Newsletter.objects.filter(status=2))

    context = {
        'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('-show')[:6],
        'lenPhone':lenPhone,
        'lenEmail':lenEmail,
        'NewsLeter':Newsletter.objects.filter(status=1),
        'NewsLeterl':Newsletter.objects.filter(status=2),
    }
    return render(request,'back/home.html',context)
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('panel')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('panel')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'logIn/login.html', context)
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for '+ user)

				return redirect('loginPage')


		context = {
            'form':form
            }
		return render(request, 'logIn/logUp.html', context)


def logoutUser(request):
	logout(request)
	return redirect('loginPage')
def news_letter(request) :


    if request.method == 'POST' :

        txt = request.POST.get('txt')

        res = txt.find('@')

        if int(res) != -1 :
            b = Newsletter(txt=txt,status=1)
            b.save()
        else:

            try:

                int(txt)
                b = Newsletter(txt=txt,status=2)
                b.save()

            except:

                return redirect('home')


    return redirect('home')
