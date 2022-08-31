from django.db import models

# Create your models here.


from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
      verbose_name = "artiste"
    def __str__(self):
      return self.name
      
class Person(models.Model):
    name = models.CharField(max_length=140, blank=True, null=True)
    def __str__(self):
        return self.name