from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from charts.models import Ip_address,SocialMedia
import requests


def ip_to_country(ip):
    url = "https://freegeoip.app/json/?" + ip
    headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }
    response = requests.request("GET", url, headers=headers)
    return response.json()['country_name']

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def visitor_modeling(request):
    ip=get_client_ip(request)
    country=ip_to_country(ip)
    print(ip,country)
    visitor_ip = Ip_address()
    visitor_ip.ip=ip
    visitor_ip.country=country

    visitor_ip.save()

def home(request ,ref=5):
    # 1 for facebook
    # 2 for instagram
    # 3 for twitter
    # 4 youtube
    # 5 other
    if (request.method == 'POST'):
        print("In")
        print(requests.POST)
        #email-form
    print("out")
    social_name=""
    if(ref == 1):
        social_name='facebook'
    elif (ref == 2 ):
        social_name='instagram'
    elif (ref == 3):
        social_name='twitter'
    elif (ref == 4):
        social_name='youtube'
    elif (ref == 5):
        social_name='other'
    else :
        return Http404
    t = SocialMedia.objects.get(name=social_name)
    t.count +=1
    t.save()
    visitor_modeling(request)
    return render(request,'home.html')

def features(request):
    visitor_modeling(request)
    return render(request,'features.html')
def about(request):
    visitor_modeling(request)
    return render(request,'about.html')
def contact(request):
    visitor_modeling(request)
    return render(request,'contact.html')



