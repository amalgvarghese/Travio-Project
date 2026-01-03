from django.shortcuts import render

from django.views import View

# Create your models here.

class HomeView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'home.html')