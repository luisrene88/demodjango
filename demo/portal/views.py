from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from portal.models import UserProfile, Empresa
from django import forms as _forms
import account.views
import account.forms
# Create your views here.
class SignupForm(account.forms.SignupForm):
    empresa = _forms.ModelChoiceField(queryset=Empresa.objects.all())

class Index(TemplateView):
    #template_name = 'index.html'
    def get(self, request):
        #if request.user.is_authenticated:
        return HttpResponseRedirect('/admin/')

class SignupView(account.views.SignupView):
    #template_name = 'index.html'
    form_class = SignupForm
