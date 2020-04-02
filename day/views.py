from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse,JsonResponse
from django import forms
from .models import UserReport
import datetime
# Create your views here.


class UserForm(forms.Form):

    name = forms.CharField(required=True,error_messages={"required": "该字段不能为空"})
    age = forms.IntegerField(min_value=0,max_value=100,required=True,error_messages={"required": "该字段不能为空", 'invalid': "格式错误"})
    address = forms.CharField(required=True,error_messages={"required": "该字段不能为空"})
    tempture = forms.DecimalField(max_digits=3, decimal_places=1,required=True,error_messages={"required": "该字段不能为空", 'invalid': "格式错误"})

class Index(View):
    #每日数据上报页面

    def get(self, request):
        return render(request,'day.html',locals())

    def post(self, requset):
        form = UserForm(requset.POST)
        if form.is_valid():
            UserReport.objects.create(
                age = requset.POST.get('age'),
                name = requset.POST.get('name'),
                address = requset.POST.get('address'),
                tempture = requset.POST.get('tempture'),
                date = datetime.datetime.now().date(),
            )
        else:
            return JsonResponse({'status': 'error'})
        return JsonResponse({'status': 'ok'})

class Success(View):
    def get(self,request):
        return render(request,'success.html')

class Error(View):
    def get(self,request):
        return render(request,'error.html')