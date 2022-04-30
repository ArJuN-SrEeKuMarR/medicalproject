from django.db import models

# Create your models here.
class medicine(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='images',null=True)

    def __str__(self):
        return self.name