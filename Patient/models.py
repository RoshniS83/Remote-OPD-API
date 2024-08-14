from django.db import models

# Create your models here.
class Patientopdform(models.Model):
          srNo = models.AutoField(db_column='srNo', primary_key=True)  # Field name made lowercase.
          patientName = models.CharField(db_column='patientName', max_length=100, blank=True,
                                         null=True)  # Field name made lowercase.
          date = models.DateField(blank=True, null=True)
          villageName = models.CharField(db_column='villageName', max_length=100, blank=True,
                                         null=True)  # Field name made lowercase.
          category = models.CharField(max_length=20, blank=True, null=True)
          gender = models.CharField(max_length=20, blank=True, null=True)
          age = models.IntegerField(blank=True, null=True)
          day = models.CharField(max_length=20, blank=True, null=True)
          month = models.CharField(max_length=20, blank=True, null=True)
          ageGroup = models.CharField(db_column='ageGroup', max_length=50, blank=True,
                                      null=True)  # Field name made lowercase.
          week = models.IntegerField(blank=True, null=True)
          mobileNo = models.BigIntegerField(db_column='mobileNo', blank=True,
                                            null=True)  # Field name made lowercase.
          signSymptoms = models.TextField(db_column='signSymptoms', blank=True, null=True)  # Field name made lowercase.
          physicalExamination = models.TextField(db_column='physicalExamination', blank=True,
                                                 null=True)  # Field name made lowercase.
          investigation = models.TextField(blank=True, null=True)
          diagnosis = models.TextField(blank=True, null=True)
          prescribedMedicine1 = models.TextField(db_column='prescribedMedicine1', blank=True,
                                                 null=True)  # Field name made lowercase.
          prescribedMedicine2 = models.TextField(db_column='prescribedMedicine2', blank=True,
                                                 null=True)  # Field name made lowercase.
          dosage = models.TextField(blank=True, null=True)
          treatmentRemark = models.TextField(db_column='treatmentRemark', blank=True,
                                             null=True)  # Field name made lowercase.

          class Meta:
                    db_table = 'patientopdform'
