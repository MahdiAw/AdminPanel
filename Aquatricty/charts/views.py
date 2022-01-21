from django.contrib.admin.decorators import register
from django.shortcuts import render
from .models import Emails, SocialMedia,Ip_address
import pandas as pd
import plotly.express as px
import requests

# Create your views here.
def get_social_data():
    items = list(SocialMedia.objects.all().values())
    df = pd.DataFrame(items)
    social_name= df['name'].tolist()
    social_count  = df['count'].tolist()
    social_date  = df['date'].tolist()
    
    
    social_data = {
        'social_name':social_name,
        'social_count':social_count,
        'date':social_date,
    }
    return social_data


def get_first_client_data():
    items = list(Ip_address.objects.all().values())[::-1][:6]
    df = pd.DataFrame(items)
    print(df)
    ips = df['ip'].tolist()
    countrys  = df['country'].tolist()
    date  = df['date'].tolist()

    ips_data = {
        'ips':ips,
        'countrys':countrys,
        'ip_date':date,

    }
    return ips_data

def get_all_client_data():
    items = list(Ip_address.objects.all().values())
    df = pd.DataFrame(items)

    ips = df['ip'].tolist()
    countrys  = df['country'].tolist()
    date  = df['date'].tolist()
    id = df.index
    ips_data = {
        'id':id,
        'ips':ips,
        'countrys':countrys,
        'date':date,

    }
    return ips_data
def get_email():
    items = list(Emails.objects.all().values())
    df = pd.DataFrame(items)


def get_users(dataset):
    return len(dataset)
    
def barChart(request):
    return render(request,'charts/barChart.html',context=get_social_data())
   





