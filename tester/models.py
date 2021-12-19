from django.db import models
from datetime import date
# Create your models here.
CHOICES = [('A','A'),('B','B'),('C','C'),('D','D')]
class Question(models.Model):
    topic = models.CharField(max_length=32)
    imageUrl = models.URLField(max_length=256)
    optionA = models.CharField(max_length=1,default='A')
    optionB = models.CharField(max_length=1,default='B')
    optionC = models.CharField(max_length=1,default='C')
    optionD = models.CharField(max_length=1,default='D')
    correctOption = models.CharField(max_length=1,choices=CHOICES,)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.topic +" #" + str(self.id)

    def age(self):
        return (date.today() - self.updated).days