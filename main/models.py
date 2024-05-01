from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class GoldRate(models.Model):
    akgsma = models.IntegerField()
    kjf = models.IntegerField()
    s_bhavan = models.IntegerField()
    thrichur = models.IntegerField()
    kgsda = models.IntegerField()
    options = (
        ('22k','22k'),
        ('24k','24k')
    )
    category = models.CharField(max_length=50,choices=options)
    added_date = models.DateField()
    change = models.IntegerField(null=True)
    def __str__(self) -> str:
        return f'{self.added_date}'
    
class Investment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    organization = models.ForeignKey(GoldRate,on_delete=models.CASCADE)
    price  = models.FloatField()
    