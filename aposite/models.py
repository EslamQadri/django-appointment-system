from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class appointments(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    Reserve = models.DateField()
    Cancel =models.BooleanField(default=False)
    approve= models.BooleanField(default=False)
    make_as_missed = models.BooleanField(default=False)
    make_as_finished= models.BooleanField(default=False)
    