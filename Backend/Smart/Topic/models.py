from django.db import models
from Chapter.models import Chapters

# Create your models here.
class Topics(models.Model):
    cid = models.ForeignKey(Chapters, on_delete=models.CASCADE, related_name='topics')
    topic = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField()