from django.db import models

# Create your models here.
class Company(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    reg_code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    address = models.TextField()
    city = models.CharField(max_length=50)
    paket_id = models.IntegerField()
    post_code = models.IntegerField()
    phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=30)
    npwp = models.CharField(max_length=20, blank=True)
    tax_person_name = models.CharField(max_length=30, blank=True)
    tax_person_npwp = models.CharField(max_length=20, blank=True)
    bpjstk = models.CharField(max_length=200)
    jkk = models.IntegerField()
    jht_emp_paid_flag = models.IntegerField(blank=True, null=True)
    bpjsk_emp_paid_flag = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    use_expired_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_company'

class NationalHoliday(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    date = models.DateField()
    description = models.CharField(max_length=40)
    flag = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_national_holiday'
