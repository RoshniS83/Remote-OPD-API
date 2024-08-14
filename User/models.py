from django.db import models

# Create your models here.
class User(models.Model):
          uid = models.AutoField(primary_key=True)
          username = models.CharField(max_length=30, blank=True, null=True)
          password = models.CharField(max_length=30, blank=True, null=True)
          mobileno = models.CharField(max_length=20, blank=True, null=True)
          role = models.CharField(max_length=30, blank=True, null=True)

          class Meta:
                    db_table = 'user'
