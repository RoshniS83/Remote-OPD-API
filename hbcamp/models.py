from django.db import models

class HBCamp(models.Model):
          SrNo = models.AutoField(primary_key=True)
          village = models.CharField(max_length=250)
          date = models.DateField()
          year = models.IntegerField()
          month = models.CharField(max_length=50)
          name = models.CharField(max_length=255, blank=True, null=True)
          gender = models.CharField(max_length=2)
          contact = models.CharField(max_length=20, blank=True, null=True)
          subvillage = models.CharField(max_length=255, blank=True, null=True)
          age = models.IntegerField(blank=True, null=True)
          HB = models.FloatField(blank=True, null=True)
          HBReadings = models.CharField(max_length=255, blank=True, null=True)
          client_name = models.CharField(max_length=200, blank=True, null=True)

          class Meta:
                    db_table = 'hbcamp'
