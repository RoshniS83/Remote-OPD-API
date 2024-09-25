from django.db import models

# Create your models here.
class Client(models.Model):
          client_id = models.AutoField(primary_key=True)
          client_name = models.TextField(blank=True, null=True)

          class Meta:
                    db_table = 'client'
