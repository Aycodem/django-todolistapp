from django.db import models
from django.contrib.auth.models import User
# Create your models here.






class Customer(models.Model):
    user=models.CharField(max_length=300 )
    
    def __str__(self):
        return str(self.user)


class Note(models.Model):
    customer=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    text =models.TextField(help_text='please input some stuff')
    
    
    def __str__(self):
        return str(self.customer)