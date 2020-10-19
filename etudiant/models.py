from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Filier(models.Model):
    name = models.CharField(max_length=30, default='-')
    title = models.CharField(max_length=30)
    pic  = models.ImageField(default="filier.png", null=True, blank=True)
    count = models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    def __str__(self):
        return self.name
class Semmester(models.Model):

    name = models.CharField(max_length=150)
    purname = models.CharField(max_length=150,default='purname')
    nameUrl = models.CharField(max_length=150,default='nameUrl')
    filier = models.ForeignKey(Filier, null=True, on_delete= models.SET_NULL)
    count = models.IntegerField(default=0)
    filierId = models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name


class Module(models.Model):

    name = models.CharField(max_length=150)
    nameUrl = models.CharField(max_length=150,default='nameUrl')
    nameSem = models.CharField(max_length=150,default='nameSem')
    semmester = models.ForeignKey(Semmester, null=True, on_delete= models.SET_NULL)
    semmesterUrl = models.CharField(max_length=150,default='semmesterUrl')
    filier = models.CharField(max_length=150 , default='-')
    semmesteriD = models.IntegerField(default=0)
    filieriD = models.IntegerField(default=0)
    ccount = models.IntegerField(default=0)
    Tdcount = models.IntegerField(default=0)
    tpcount = models.IntegerField(default=0)
    ecount = models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    Lasshow = models.IntegerField(default=0)

    def __str__(self):
        return  self.name

class Cours(models.Model):
    name = models.CharField(max_length=150)
    pdf=models.FileField(upload_to="coure")
    # pdf=models.CharField(max_length=150,default="pdfUrl")
    moduleid = models.IntegerField(default=0)
    module = models.CharField(max_length=150,default="module")
    moduleUrl = models.CharField(max_length=150,default="moduleUrl")
    semmester = models.CharField(max_length=150,default="semmester")
    semmesterUrl= models.CharField(max_length=150,default="semmesterUrl")
    semmesterID = models.IntegerField(default=0)
    filier = models.CharField(max_length=150,default="filier")
    filierID = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s %s" % (self.name, self.semmester, self.filier)


class TD(models.Model):
    name = models.CharField(max_length=150)
    pdf=models.FileField(upload_to="td")
    # pdf = models.CharField(max_length=150,default="pdfUrl")
    moduleid = models.IntegerField(default=0)
    module = models.CharField(max_length=150,default="module")
    moduleUrl = models.CharField(max_length=150,default="moduleUrl")
    semmester = models.CharField(max_length=150,default="semmester")
    semmesterUrl= models.CharField(max_length=150,default="semmesterUrl")
    semmesterID = models.IntegerField(default=0)
    filier = models.CharField(max_length=150,default="filier")
    filierID = models.IntegerField(default=0)

    def __str__(self):
        return  "%s %s %s" % (self.name, self.semmester, self.filier)

class TP(models.Model):
    name = models.CharField(max_length=150)
    pdf=models.FileField(upload_to="TPs")
    # pdf = models.CharField(max_length=150,default="pdfUrl")
    moduleid = models.IntegerField(default=0)
    module = models.CharField(max_length=150,default="module")
    moduleUrl = models.CharField(max_length=150,default="moduleUrl")
    semmester = models.CharField(max_length=150,default="semmester")
    semmesterUrl= models.CharField(max_length=150,default="semmesterUrl")
    semmesterID = models.IntegerField(default=0)
    filier = models.CharField(max_length=150,default="filier")
    filierID = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s %s" % (self.name, self.semmester, self.filier)


class Exam(models.Model):
    name = models.CharField(max_length=150)
    pdf=models.FileField(upload_to="EXAMs")
    # pdf = models.CharField(max_length=150,default="pdfUrl")
    moduleid = models.IntegerField(default=0)
    module = models.CharField(max_length=150,default="module")
    moduleUrl = models.CharField(max_length=150,default="moduleUrl")
    semmester = models.CharField(max_length=150,default="semmester")
    semmesterUrl= models.CharField(max_length=150,default="semmesterUrl")
    semmesterID = models.IntegerField(default=0)
    filier = models.CharField(max_length=150,default="filier")
    filierID = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s %s" % (self.name, self.semmester, self.filier)

