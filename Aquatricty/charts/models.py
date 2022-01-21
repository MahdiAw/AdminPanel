from django.db import models


# Create your models here.
class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField()
    date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name + " : " + str(self.count)
class Ip_address(models.Model):
    ip = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    def __str__(self) -> str:
        return self.country + " : " + self.country

class Emails(models.Model):
    emails = models.CharField(max_length=50)
    def __str__(self) -> str:
        return Emails.emails