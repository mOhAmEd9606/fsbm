from django.forms import ModelForm,ModelChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class AddfillierForm(ModelForm):
	class Meta:
		model = Filier
		fields = ['name', 'title','pic']

class AddSemmesterForm(ModelForm):
	class Meta:
		model = Semmester
		fields = ['name','filier']
class AddModuleForm(ModelForm):
	class Meta:
		model = Module
		fields = ['name','semmester']
class AddfCoureForm(ModelForm):
	class Meta:
		model = Cours
		fields = ['name','pdf']
class AddTdForm(ModelForm):
	class Meta:
		model = TD
		fields = ['name','pdf']
class AddtpForm(ModelForm):
	class Meta:
		model = TP
		fields = ['name','pdf']
class AddexamForm(ModelForm):
	class Meta:
		model = Exam
		fields = ['name','pdf']

