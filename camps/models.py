from django.db import models

# Create your models here.
class Camps(models.Model):
    name = models.TextField(blank=True, null=True)

    class Meta:

        db_table = 'camps'