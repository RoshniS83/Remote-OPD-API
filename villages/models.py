from django.db import models

# Create your models here.
class Villages(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    vnames = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'villages'
