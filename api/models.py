from pickle import TRUE
from django.db import models

class Reservation(models.Model):
    # Exhibit_Choices = (('전시1','전시1'),('전시2','전시2'),('전시3','전시3'))
    # Exhibit = models.CharField(null=True, max_length=10, choices=Exhibit_Choices)
    Day_Choices = (('9월 3일','9월 3일'),('9월 4일','9월 4일'),('9월 17일','9월 17일'),('9월 18일','9월 18일'),('9월 24일','9월 24일'),('9월 25일','9월 25일'))
    Day = models.CharField(null=True, max_length=10, choices=Day_Choices)
    Person_Choices = (('1명','1명'),('2명','2명'))
    Person = models.CharField(null=True, max_length=10, choices=Person_Choices)
    Time_Choices = (('12시','12시'),('12시 30분','12시 30분'),('13시','13시'),('13시 30분','13시 30분'),('14시','14시'),('14시 30분','14시 30분'),('15시','15시'),('15시 30분','15시 30분'),('16시','16시'),('16시 30분','16시 30분'),('17시','17시'),('17시 30분','17시 30분'),('18시','18시'),('18시 30분','18시 30분'), ('19시','19시'), ('19시 30분','19시 30분'), ('20시','20시'))
    Time = models.CharField(null=True, max_length=10, choices=Time_Choices)
    Name = models.TextField(null=True)
    Phone = models.TextField(null=True)
    Dance = models.BooleanField(null=True)
    Personal = models.BooleanField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.Time[0:50]

class Contact(models.Model):
    contact = models.TextField(null=True)

class Image(models.Model):
    photo = models.ImageField(
        blank=True, upload_to='oumtt/exhibit_program/'
    )
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)