from django.db import models

class Megacamp(models.Model):
    srno = models.AutoField(db_column='SrNo', primary_key=True)  # Field name made lowercase.
    village = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=60, blank=True, null=True)
    day = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)
    villagename = models.CharField(db_column='villageName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    bp = models.CharField(db_column='BP', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pulse = models.IntegerField(blank=True, null=True)
    temperature = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    bloodtest = models.TextField(blank=True, null=True)
    hb = models.DecimalField(db_column='HB', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    xray = models.TextField(db_column='XRay', blank=True, null=True)  # Field name made lowercase.
    ecg = models.CharField(db_column='ECG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    eyetest = models.CharField(max_length=255, blank=True, null=True)
    audiometry = models.TextField(blank=True, null=True)
    spirometry = models.TextField(blank=True, null=True)
    breastcancer = models.TextField(blank=True, null=True)
    cervicalcancer = models.TextField(blank=True, null=True)
    oralcancer = models.TextField(blank=True, null=True)
    tb = models.CharField(db_column='TB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    client_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'megacamp'

