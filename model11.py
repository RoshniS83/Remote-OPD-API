# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adcamp(models.Model):
    srno = models.AutoField(db_column='SrNo', primary_key=True)  # Field name made lowercase.
    village = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.CharField(max_length=60, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    standard = models.CharField(max_length=45, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    hb = models.DecimalField(db_column='HB', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    villagename = models.CharField(db_column='villageName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hbreadings = models.CharField(db_column='HBReadings', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bmi = models.DecimalField(db_column='BMI', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    bmireadings = models.CharField(db_column='BMIReadings', max_length=100, blank=True, null=True)  # Field name made lowercase.
    client_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adcamp'


class Camps(models.Model):
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'camps'


class Disease(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'disease'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Eyecamp(models.Model):
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
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    opinion = models.TextField(db_column='Opinion', blank=True, null=True)  # Field name made lowercase.
    client_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eyecamp'


class Hbcamp(models.Model):
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
    hb = models.FloatField(db_column='HB', blank=True, null=True)  # Field name made lowercase.
    hbreadings = models.CharField(db_column='HBReadings', max_length=255, blank=True, null=True)  # Field name made lowercase.
    client_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hbcamp'


class Medicines(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicines'


class Patientopdform(models.Model):
    srno = models.AutoField(db_column='srNo', primary_key=True)  # Field name made lowercase.
    patientname = models.CharField(db_column='patientName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    village = models.CharField(max_length=255, blank=True, null=True)
    villagename = models.CharField(db_column='villageName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    day = models.CharField(max_length=20, blank=True, null=True)
    month = models.CharField(max_length=20, blank=True, null=True)
    agegroup = models.CharField(db_column='ageGroup', max_length=50, blank=True, null=True)  # Field name made lowercase.
    week = models.IntegerField(blank=True, null=True)
    mobileno = models.CharField(db_column='mobileNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    signsymptoms = models.TextField(db_column='signSymptoms', blank=True, null=True)  # Field name made lowercase.
    physicalexamination = models.CharField(db_column='physicalExamination', max_length=255, blank=True, null=True)  # Field name made lowercase.
    investigation = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    diagnosis2 = models.TextField(blank=True, null=True)
    prescribedmedicine1 = models.CharField(db_column='prescribedMedicine1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prescribedmedicine2 = models.CharField(db_column='prescribedMedicine2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prescribedmedicine3 = models.CharField(db_column='prescribedMedicine3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prescribedmedicine4 = models.CharField(db_column='prescribedMedicine4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(max_length=255, blank=True, null=True)
    treatmentremark = models.TextField(db_column='treatmentRemark', blank=True, null=True)  # Field name made lowercase.
    client_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patientopdform'


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    mobileno = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Villages(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    vnames = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'villages'
