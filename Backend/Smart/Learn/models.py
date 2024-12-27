from django.db import models

# Create your models here.
class Subjects(models.Model):# Replace 'default_value' with your desired default
    subjectname = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __int__(self):
        return self.id