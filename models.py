from django.db import models
from django.utils.text import slugify

# Create your models here.
class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)


     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email

class Newpage(models.Model):
       title = models.CharField(max_length=200)
       content = models.TextField()
       slug = models.SlugField(unique=True)

       def __str__(self):
        return self.title

       def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # You'll need to import slugify
        super().save(*args, **kwargs)










