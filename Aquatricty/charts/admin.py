from django.contrib import admin
from .models import Ip_address, SocialMedia,Emails
# Register your models here.
admin.site.register(SocialMedia)
admin.site.register(Ip_address)
admin.site.register(Emails)