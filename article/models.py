from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=400 , default="name")
    count = models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    def __str__(self):
        return self.name
class Article(models.Model):
    name = models.CharField(max_length=400 , default="name")
    artID = models.CharField(max_length=15)
    cat = models.CharField(max_length=400 , default="cat")
    catid = models.IntegerField(default=0)
    discripton = models.TextField(default="discription")
    artbody = models.TextField(default="discription")
    pic  = models.ImageField(upload_to="Article",default="art.png", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    writer = models.CharField(max_length=50)
    show = models.IntegerField(default=0)
    act = models.IntegerField(default=0)
    rand = models.IntegerField(default=0)
    def __str__(self):
        return self.name
class Links(models.Model):
    name = models.CharField(max_length=400 , default="name")
    Artname = models.ForeignKey(Article, null=True, on_delete= models.SET_NULL)
    artId = models.CharField(max_length=400 , default="artId")
    link = models.CharField(max_length=400 , default="link")
    def __str__(self):
        return self.name
class Tags(models.Model):
    name = models.CharField(max_length=400 , default="name")
    Artname = models.ForeignKey(Article, null=True, on_delete= models.SET_NULL)
    artId = models.CharField(max_length=400 , default="artId")
    def __str__(self):
        return self.name


