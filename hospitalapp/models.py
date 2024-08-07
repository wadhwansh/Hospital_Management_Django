from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class login(models.Model):
      user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)


class Contact(models.Model):
      Name=models.CharField(max_length=50)
      Email=models.EmailField(unique=True,max_length=50)
      Subject=models.CharField(max_length=50)
      Phone=models.IntegerField()
      Message=models.TextField()
      

class Booking(models.Model):
      Department_Choices=[
            ('cardiology','Cardiology'),
            ('Derma','Dermatology and Cosmetology'),
            ('Gen','General Surgery'),
            ('Neuro','Neurology'),
            ('Health','Health Checkup Packages')
      ]
      Time_choices=[
            ("8 AM - 10 AM","8 AM - 10 AM"),
		("10 AM - 12 PM" ,"10 AM - 12 PM"),
		("12 PM - 2 PM","12 PM - 2 PM"),
		 ("2 PM - 4 PM","2 PM - 4 PM"),
		("4 PM - 6 PM" ,"4 PM - 6 PM"),
		("6 PM - 8 PM" ,"6 PM - 8 PM"),
		(" 8 PM - 10 PM","8 PM - 10 PM"),
      ]
      user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
      Name = models.CharField(max_length=50)
      Email = models.EmailField(unique=True)
      Purpose = models.TextField(null=False)
      Phone = models.IntegerField(null=False)
      Surgury = models.CharField( max_length=50,null=False,choices=Department_Choices)
      Date = models.DateField(null=False)
      Time = models.CharField(max_length=50,null=False,choices=Time_choices)
      
      
      
      
      