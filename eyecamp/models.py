from django.db import models

# Create your models here.
class EyeCamp(models.Model):
    srno = models.AutoField(db_column='SrNo', primary_key=True)  # Field name made lowercase.
    village = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)
    subvillage = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    opinion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'eyecamp'