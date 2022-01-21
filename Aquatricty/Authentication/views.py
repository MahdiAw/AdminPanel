


from Aquatricty.views import get_client_ip
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse, request, response,HttpResponseRedirect
from charts.views import get_all_client_data, get_social_data,get_first_client_data


user = "mahdi"
password ="1234"

def login_view(request):
    wrong="We\'ll never share your password with anyone else"
    contex={}
    if (request.method == 'POST'):
        auth_user = request.POST['username']
        auth_password =request.POST['password']

        if(auth_password==password and auth_user==user):
            contex= get_social_data()
            contex.update(get_first_client_data())
            ips_nb = len(contex['ips'])
            contex['ips']=zip(contex['ips'],contex['countrys'],contex['ip_date'])
            contex['totalusers']=str(sum(contex['social_count']))
            print(contex)
            return render(request,'index.html',context=contex)
        else:
            wrong="wrong password or user name"

    return render(request,'login.html',context={'wrong':wrong})

def  ip_table(request):
    contex = get_all_client_data()
    contex['datas'] = zip(contex['id'],contex['ips'],contex['countrys'],contex['date'])
    return render(request,'ip_table.html',context=contex)
def  links(request):
    return render(request,'links.html')
def map(request):
    return render(request,'map.html')
def email(request):
    return render(request,'emails.html')
