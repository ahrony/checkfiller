from datetime import date
from django.db import models


# Create your models here.


class Checkdetails(models.Model):
    name = models.CharField(max_length=100,verbose_name='Pay To',blank=True,null=True)
    total_ammount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='TK',blank=True,null=True)
    ammount_in_word = models.CharField(max_length=100,blank=True,null=True)
    date = models.DateField(blank=True,null=True)

    def __unicode__(self):
    	return self.name





