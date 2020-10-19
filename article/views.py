from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from .models import *
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from django.contrib.auth.models import User, Group, Permission
from .forms import *
from etudiant.models import *
import string
import random
# Create your views here.

"""___-Cat-___"""
def _CatManage(request):
    form = CatForm()
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            mes = (f' {name} Create Succesfully ')
            messages.success(request, mes)
        else : 
            mes = (' Error !! ')
            messages.error(request, mes)
        return redirect('CatManage')
    context = {
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('-show')[:6],
        'catagury':Cat.objects.all(),
        'form':form
    }
    return render(request,'back/article/list.html',context)

def ArticleAdmin(request,artID):
    print('---------------------------p----------------------------------')
    print(artID)
    print('hh')
    print('-------------------------------------------------------------')
    size=9
    chars=string.ascii_uppercase + string.digits
    RandId = ''.join(random.choice(chars) for _ in range(size))
    form = ArticleForm()
    formAdlink = lincksForm()
    formAdtag = TagsForm()
    if request.method == "POST":
        formAdtag = TagsForm(request.POST)
        if formAdtag.is_valid():
            formAdtag.save(commit=False)
            na = formAdtag.cleaned_data['name']
            Artn = formAdtag.cleaned_data['Artname']
            ArtID = Article.objects.get(name=Artn).artID
            TT = Tags(artId=ArtID,name=na,Artname=Artn)
            TT.save()

        formAdlink = lincksForm(request.POST)
        if formAdlink.is_valid():
            formAdlink.save(commit=False)
            na = formAdlink.cleaned_data['name']
            Artn = formAdlink.cleaned_data['Artname']
            lik = formAdlink.cleaned_data['link']
            ArtID = Article.objects.get(name=Artn).artID
            kk = Links(artId=ArtID,name=na,link=lik,Artname=Artn)
            kk.save()

        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            print('Is valide')
            name = form.cleaned_data['name']
            artBy = form.cleaned_data['artbody']
            pic = form.cleaned_data['pic']
            catagury = Cat.objects.get(name=artID).name
            catId = Cat.objects.get(name=artID).pk
            discription = artBy[:150]
            writer= User.username
            print(f'User :'+ str(writer))
            arte = Article(name=name,artID=RandId,cat=catagury,catid=catId,discripton=discription,artbody=artBy,pic=pic,writer=writer)
            arte.save()
            count = len(Article.objects.filter(cat=artID,catid=catId))
            artCount = Cat.objects.get(name=artID)
            artCount.count = count
            artCount.save()

            
            mes = (' Created Succesfully ')
            messages.success(request, mes)

    cat = Cat.objects.get(name=artID)
    articlee = Article.objects.filter(cat=artID)
    Lin = Links.objects.all()
    tags = Tags.objects.all()
    context = {
        'form':form,
        'Articles':articlee,
        'cat':cat,
        'formAdlink':formAdlink,
        'Links':Lin,
        'formAdtag':formAdtag,
        'tags':tags,
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('-show')[:6],
    }
    responce = render(request,'back/article/art.html',context)
    return responce


def ArtDel(request, pk):

    order = Article.objects.get(id=pk)
    order.delete()
    count = len(Article.objects.filter(pk=pk))
    moduleid=order.catid
    modName= Cat.objects.get(pk=moduleid)
    modName.count = count
    modName.save()
    name = order.name
    nameurl = order.cat
    mes = (f' {name} Deleted Succesfully ')
    messages.success(request, mes)
    return redirect('ArticleAdmin',artID=nameurl)   
def Articlepage(request):
    context = {
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('-show')[:6],
        'ArticlePop':Article.objects.all().order_by('-show')[:6],
        'articles' : Article.objects.filter(),
        'Filiernavebar': Filier.objects.all().order_by('pk'),

    }
    responce = render(request,'front/ArticlePage.html',context)
   
    return responce
def Catpage(request,catt):
    context = {
        'catname':catt,
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('-show')[:6],
        'ArticlePop':Article.objects.all().order_by('-show')[:5],
        'articles' : Article.objects.filter(cat=catt),
        'Filiernavebar': Filier.objects.all().order_by('pk'),

    }
    responce = render(request,'front/CatPage.html',context)
    return responce
def ArticleDetail(request,ArtId):
    Upcount=Article.objects.get(artID=ArtId)
    Upcount.show = Upcount.show + 1
    Upcount.save()
    
    context = {
        'Tags': Tags.objects.all(),
        'Links':Links.objects.all(),
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('-show')[:6],
        'articles' : Article.objects.filter(artID=ArtId),
        'Filiernavebar': Filier.objects.all().order_by('pk'),
        'ArticlePop':Article.objects.all().order_by('-show')[:3],
        }

    responce = render(request,'front/articleDetail.html',context)
    return responce


# Catagury : 
    # Cat Detaill
def _CatManage(request):
    form = CatForm()
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            mes = (f' {name} Create Succesfully ')
            messages.success(request, mes)
        else : 
            mes = (' Error !! ')
            messages.error(request, mes)
        return redirect('_CatManage')
    
    order = Cat.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('_CatManage')
    context = {
        'item':order,
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('-show')[:6],
        'catagury':Cat.objects.all(),
        'form':form
    }
    return render(request,'back/article/list.html',context)
    # Add,context
    # Del	
   
# Article :
    # Art Detail:
def _Art_Detail(request,cat,ArtId):
    context = {
        'articles' : Article.objects.filter(cat=cat,artID=ArtId),
         'Cats': Cat.objects.all().order_by('pk'),
        'Filiers': Filier.objects.all(),
         'Semmesters': Semmester.objects.all(),
        'modules':Module.objects.all().order_by('-show')[:6],
        }
    responce = render(request,'back/article/ArtDetail.html',context)
    return responce
    # Add
    # Del