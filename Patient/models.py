from django.db import models

# Create your models here.
# class Patientopdform(models.Model):
#           srNo = models.AutoField(db_column='srNo', primary_key=True)  # Field name made lowercase.
#           patientName = models.CharField(db_column='patientName', max_length=100, blank=True,
#                                          null=True)  # Field name made lowercase.
#           date = models.CharField(max_length=100, blank=True, null=True)
#           villageName = models.CharField(db_column='villageName', max_length=100, blank=True,
#                                          null=True)  # Field name made lowercase.
#           category = models.CharField(max_length=20, blank=True, null=True)
#           gender = models.CharField(max_length=20, blank=True, null=True)
#           age = models.IntegerField(blank=True, null=True)
#           day = models.CharField(max_length=20, blank=True, null=True)
#           month = models.CharField(max_length=20, blank=True, null=True)
#           ageGroup = models.CharField(db_column='ageGroup', max_length=50, blank=True,
#                                       null=True)  # Field name made lowercase.
#           week = models.IntegerField(blank=True, null=True)
#           mobileNo = models.CharField(db_column='mobileNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
#           signSymptoms = models.TextField(db_column='signSymptoms', blank=True, null=True)  # Field name made lowercase.
#           physicalExamination = models.TextField(db_column='physicalExamination', blank=True,
#                                                  null=True)  # Field name made lowercase.
#           investigation = models.TextField(blank=True, null=True)
#           diagnosis = models.TextField(blank=True, null=True)
#           prescribedMedicine1 = models.TextField(db_column='prescribedMedicine1', blank=True,
#                                                  null=True)  # Field name made lowercase.
#           prescribedMedicine2 = models.TextField(db_column='prescribedMedicine2', blank=True,
#                                                  null=True)  # Field name made lowercase.
#           dosage = models.TextField(blank=True, null=True)
#           treatmentRemark = models.TextField(db_column='treatmentRemark', blank=True,
#                                              null=True)  # Field name made lowercase.
#
#           class Meta:
#                     db_table = 'patientopdform'

# class Patientopdform(models.Model):
#     sr_no = models.IntegerField(blank=True, null=True)
#     patient_name = models.CharField(max_length=255, blank=True, null=True)
#     date = models.DateField(blank=True, null=True)
#     village_name = models.CharField(max_length=255, blank=True, null=True)
#     nf_scr = models.CharField(max_length=255, blank=True, null=True)
#     gender = models.CharField(max_length=50, blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)
#     day = models.IntegerField(blank=True, null=True)
#     month = models.IntegerField(blank=True, null=True)
#     age_group = models.CharField(max_length=50, blank=True, null=True)
#     week = models.IntegerField(blank=True, null=True)
#     mobile_no = models.CharField(max_length=50, blank=True, null=True)
#     signs_and_symptoms = models.TextField(blank=True, null=True)
#     physical_examination_and_finding = models.TextField(blank=True, null=True)
#     investigation = models.TextField(blank=True, null=True)
#     diagnosis = models.TextField(blank=True, null=True)
#     prescribed_medicine_1 = models.CharField(max_length=255, blank=True, null=True)
#     prescribed_medicine_2 = models.CharField(max_length=255, blank=True, null=True)
#     dosage = models.CharField(max_length=255, blank=True, null=True)
#     treatment_remark = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'patientopdform'
class Patientopdform(models.Model):
    srNo = models.AutoField(db_column='srNo', primary_key=True)  # Field name made lowercase.
    patientName = models.CharField(db_column='patientName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField()
    year = models.IntegerField()
    village = models.CharField(max_length=255, blank=True, null=True)
    villageName = models.CharField(db_column='villageName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    category = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    day = models.CharField(max_length=20, blank=True, null=True)
    month = models.CharField(max_length=20, blank=True, null=True)
    ageGroup = models.CharField(db_column='ageGroup', max_length=50, blank=True, null=True)  # Field name made lowercase.
    week = models.IntegerField(blank=True, null=True)
    mobileNo = models.CharField(db_column='mobileNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    signSymptoms = models.TextField(db_column='signSymptoms', blank=True, null=True)  # Field name made lowercase.
    physicalExamination = models.TextField(db_column='physicalExamination', blank=True, null=True)  # Field name made lowercase.
    investigation = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    prescribedMedicine1 = models.TextField(db_column='prescribedMedicine1', blank=True, null=True)  # Field name made lowercase.
    prescribedMedicine2 = models.TextField(db_column='prescribedMedicine2', blank=True, null=True)  # Field name made lowercase.
    dosage = models.TextField(blank=True, null=True)
    treatmentRemark = models.TextField(db_column='treatmentRemark', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patientopdform'
