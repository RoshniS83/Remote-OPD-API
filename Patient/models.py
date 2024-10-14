from django.db import models

class Patientopdform(models.Model):
    srNo = models.AutoField(db_column='srNo', primary_key=True)  # Field name made lowercase.
    patientName = models.CharField(db_column='patientName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    village = models.CharField(max_length=255, blank=True, null=True)
    villageName = models.CharField(db_column='villageName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    day = models.CharField(max_length=20, blank=True, null=True)
    month = models.CharField(max_length=20, blank=True, null=True)
    ageGroup = models.CharField(db_column='ageGroup', max_length=50, blank=True, null=True)  # Field name made lowercase.
    week = models.IntegerField(blank=True, null=True)
    mobileNo = models.CharField(db_column='mobileNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    signSymptoms = models.TextField(db_column='signSymptoms', blank=True, null=True)  # Field name made lowercase.
    physicalExamination = models.CharField(db_column='physicalExamination', max_length=255, blank=True, null=True)  # Field name made lowercase.
    investigation = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    diagnosis2 = models.TextField(blank=True, default='', null=True)
    prescribedMedicine1 = models.CharField(db_column='prescribedMedicine1', max_length=255, default='', blank=True, null=True)  # Field name made lowercase.
    prescribedMedicine2 = models.CharField(db_column='prescribedMedicine2', max_length=255, default='', blank=True, null=True)  # Field name made lowercase.
    prescribedMedicine3 = models.CharField(db_column='prescribedMedicine3', max_length=255, default='', blank=True, null=True)  # Field name made lowercase.
    prescribedMedicine4 = models.CharField(db_column='prescribedMedicine4', max_length=255, default='', blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(max_length=255, blank=True, null=True)
    treatmentRemark = models.TextField(db_column='treatmentRemark', blank=True, default='', null=True)  # Field name made lowercase.
    client_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patientopdform'

