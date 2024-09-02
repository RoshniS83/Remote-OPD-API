from django.db import models

# Create your models here.
class Disease(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'disease'