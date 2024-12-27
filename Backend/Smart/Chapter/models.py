from django.db import models
from Learn.models import Subjects  # Import the Subjects model

class Chapters(models.Model):  # Replace 'default_value' with your desired default
    sid = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='chapters')
    chapter = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField()

    def __int__(self):
        return self.id