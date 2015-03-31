# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Announcement(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField()
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    company_id = models.IntegerField(blank=True, null=True)
    delete_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_announcement'


class Assets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField()
    asset_category = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=50)
    date_loaned = models.DateField()
    date_returned = models.DateField()
    date_create = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_assets'


class BillingInformation(models.Model):
    billing_information_id = models.BigIntegerField(primary_key=True)
    company_id_fk = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    credit_card_number = models.CharField(max_length=30, blank=True)
    credit_card_expire_month_date = models.IntegerField(blank=True, null=True)
    credit_card_expire_year_date = models.IntegerField(blank=True, null=True)
    credit_card_bank_name = models.CharField(max_length=30, blank=True)
    credit_card_type = models.CharField(max_length=20, blank=True)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_billing_information'


class Calendar(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id_fk = models.IntegerField()
    date = models.DateField()
    amount_days = models.IntegerField()
    description = models.TextField()
    type = models.CharField(max_length=200)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    note = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'tbl_calendar'


class CalendarSelectedPerson(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    selected_person_id_fk = models.IntegerField()
    calendar_id_fk = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_calendar_selected_person'


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


class CompanyRegulation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    jkm = models.FloatField()
    jht_company = models.FloatField()
    jht_employee = models.FloatField()
    bpjsk_company = models.FloatField()
    bpjsk_employee = models.FloatField()
    jpk_married = models.FloatField()
    jpk_not_married = models.FloatField()
    commenced_date = models.DateField()
    expired_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_company_regulation'


class CompanyRegulationJkk(models.Model):
    id = models.BigIntegerField(primary_key=True)
    company_regulation_id_fk = models.ForeignKey(CompanyRegulation, db_column='company_regulation_id_fk')
    description = models.CharField(max_length=100)
    jkk = models.FloatField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_company_regulation_jkk'


class EmailRecommendation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.BigIntegerField()
    email = models.CharField(max_length=100)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_email_recommendation'


class EmergencyContact(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    relation = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_emergency_contact'


class EmployeeAllowanceDeduction(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField()
    component_id = models.IntegerField()
    mode_flag = models.IntegerField()
    tax_mode = models.IntegerField()
    amount = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_employee_allowance_deduction'


class EmployeeAllowanceDeductionHistory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    component_id = models.IntegerField()
    component_name = models.CharField(max_length=200)
    user_id = models.IntegerField()
    mode_flag = models.IntegerField()
    tax_mode = models.IntegerField()
    amount = models.FloatField(blank=True, null=True)
    cutoff_from = models.DateField(blank=True, null=True)
    cutoff_to = models.DateField(blank=True, null=True)
    period = models.DateField()
    created_date = models.DateTimeField()
    updated_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_employee_allowance_deduction_history'


class EmployeeAttendance(models.Model):
    id = models.BigIntegerField(primary_key=True)
    company_id = models.IntegerField()
    nik = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    mode = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=50)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_employee_attendance'


class EmployeeAttendanceMonthly(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.IntegerField()
    nik = models.CharField(max_length=200)
    checkin = models.TimeField()
    checkout = models.TimeField()
    overtime_duration = models.TimeField()
    date = models.DateField()
    policies_id = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_employee_attendance_monthly'


class EmployeeResign(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id_fk = models.IntegerField()
    employee_id_fk = models.IntegerField()
    reason = models.TextField()
    length_of_service = models.FloatField()
    merit_pay = models.FloatField()
    resign_date = models.DateField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_employee_resign'


class EmployeeSalaryHistory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField()
    basic_salary = models.FloatField()
    allowance_taxable = models.FloatField(blank=True, null=True)
    allowance_nontaxable = models.FloatField()
    deduction_taxable = models.FloatField(blank=True, null=True)
    deduction_nontaxable = models.FloatField()
    jkk = models.FloatField()
    jkm = models.FloatField()
    jht_employee = models.FloatField()
    jht_company = models.FloatField()
    bpjsk_employee = models.FloatField()
    bpjsk_company = models.FloatField()
    gross_monthly = models.FloatField()
    gross_yearly = models.FloatField()
    position_cost = models.FloatField()
    jht_employee_yearly = models.FloatField()
    netto_yearly = models.FloatField()
    ptkp = models.IntegerField()
    pkp = models.IntegerField()
    pph_yearly = models.FloatField()
    pph_monthly = models.FloatField()
    tax_allowance = models.FloatField()
    bonus = models.FloatField()
    thr = models.FloatField(blank=True, null=True)
    allowance_once = models.FloatField()
    deduction_once = models.FloatField()
    gross_yearly_bonus = models.IntegerField()
    position_cost_bonus = models.FloatField()
    netto_yearly_bonus = models.IntegerField()
    ptkp_bonus = models.IntegerField()
    pkp_bonus = models.IntegerField()
    pph_yearly_bonus = models.FloatField()
    pph_bonus = models.FloatField()
    tax_allowance_bonus = models.FloatField()
    pph_total = models.FloatField()
    tax_allowance_total = models.FloatField()
    overtime = models.FloatField(blank=True, null=True)
    absence = models.FloatField(blank=True, null=True)
    cutoff_from = models.DateField()
    cutoff_to = models.DateField()
    period = models.DateField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_employee_salary_history'


class Files(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id_fk = models.IntegerField()
    user_id_fk = models.IntegerField()
    flag_file = models.IntegerField()
    name_file = models.CharField(max_length=100)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_files'


class HistoryBillingTransaction(models.Model):
    history_billing_transaction_id = models.BigIntegerField(primary_key=True)
    company_id_fk = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    credit_card_number = models.CharField(max_length=30, blank=True)
    credit_card_expire_month_date = models.IntegerField(blank=True, null=True)
    credit_card_expire_year_date = models.IntegerField(blank=True, null=True)
    credit_card_bank_name = models.CharField(max_length=30, blank=True)
    credit_card_type = models.CharField(max_length=20, blank=True)
    security_number = models.CharField(max_length=10, blank=True)
    payment_due_date = models.DateField()
    total_user = models.DateField()
    price = models.FloatField()
    total_price = models.FloatField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_history_billing_transaction'


class HistoryPaymentTransaction(models.Model):
    history_payment_transaction_id = models.BigIntegerField(primary_key=True)
    history_billing_information_id_fk = models.BigIntegerField()
    payment_date = models.DateTimeField()
    total_paid = models.FloatField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_history_payment_transaction'


class Inbox(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sender_id = models.IntegerField()
    receiver_id = models.IntegerField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    inbox_type = models.IntegerField()
    fk_ref = models.IntegerField(blank=True, null=True)
    read_flag = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    delete_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_inbox'


class Job(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.IntegerField()
    job_id = models.CharField(max_length=50)
    job = models.CharField(max_length=100)
    description = models.TextField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_job'


class JobStructure(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.IntegerField()
    parent_id = models.IntegerField()
    child_id = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_job_structure'


class Migration(models.Model):
    version = models.CharField(primary_key=True, max_length=180)
    apply_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_migration'


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


class Onboarding(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.IntegerField()
    template_name = models.CharField(max_length=250)
    start_date = models.DateField()
    start_time = models.TimeField()
    format_time = models.IntegerField()
    instruction = models.TextField()
    comment = models.TextField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_onboarding'


class Organization(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.IntegerField()
    organization_id = models.CharField(max_length=50)
    organization = models.CharField(max_length=100)
    description = models.TextField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_organization'


class OrganizationStructure(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.IntegerField()
    parent_id = models.IntegerField()
    child_id = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_organization_structure'


class OvertimeMultiplier(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.IntegerField()
    multiplier_name = models.CharField(max_length=100)
    compensation_flag = models.IntegerField()
    is_used = models.IntegerField()
    override_idr = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_overtime_multiplier'


class OvertimeMultiplierStructure(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    multiplier_id = models.IntegerField()
    hour_from = models.IntegerField()
    hour_to = models.IntegerField(blank=True, null=True)
    category_flag = models.IntegerField()
    multiply = models.FloatField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_overtime_multiplier_structure'


class OvertimeRequest(models.Model):
    id = models.BigIntegerField(primary_key=True)
    company_id = models.IntegerField()
    rounding_id = models.IntegerField()
    user_id = models.IntegerField()
    description = models.TextField()
    hour = models.IntegerField()
    minutes = models.IntegerField()
    category_id = models.IntegerField()
    status_approval = models.IntegerField()
    request_date = models.DateField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_overtime_request'


class OvertimeRounding(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.IntegerField()
    from_field = models.IntegerField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.IntegerField()
    round = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_overtime_rounding'


class Paket(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    paket = models.CharField(max_length=50)
    min = models.IntegerField()
    max = models.IntegerField()
    price = models.FloatField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_paket'


class Pattern(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.IntegerField()
    pattern_name = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_pattern'


class PayrollAbsence(models.Model):
    payroll_absence_id = models.BigIntegerField(primary_key=True)
    company_id_fk = models.IntegerField()
    type = models.IntegerField()
    amount = models.FloatField(blank=True, null=True)
    date_type = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_payroll_absence'


class PayrollComponent(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.IntegerField()
    component_name = models.CharField(max_length=100)
    component_amount = models.FloatField()
    component_tax_type = models.IntegerField()
    component_type = models.IntegerField()
    component_group = models.IntegerField()
    component_occurs_type = models.IntegerField()
    component_prorate = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_payroll_component'


class PayrollComponentHistory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    component_id = models.IntegerField()
    company_id = models.IntegerField()
    component_name = models.CharField(max_length=100)
    component_amount = models.FloatField()
    component_tax_type = models.IntegerField()
    component_type = models.IntegerField()
    component_group = models.IntegerField()
    component_occurs_type = models.IntegerField()
    component_prorate = models.IntegerField(blank=True, null=True)
    cutoff_from = models.DateField(blank=True, null=True)
    cutoff_to = models.DateField(blank=True, null=True)
    period = models.DateField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_payroll_component_history'


class PayrollCutoff(models.Model):
    payroll_cufoff_id = models.BigIntegerField(primary_key=True)
    company_id_fk = models.IntegerField()
    tax_type = models.IntegerField()
    attendance_from = models.IntegerField()
    attendance_to = models.IntegerField()
    payroll_from = models.IntegerField()
    payroll_to = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_payroll_cutoff'


class PayrollProrate(models.Model):
    payroll_prorate_id = models.BigIntegerField(primary_key=True)
    company_id_fk = models.IntegerField()
    prorate_type = models.IntegerField()
    custom_number = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_payroll_prorate'


class PayrollSchedule(models.Model):
    payroll_schedule_id = models.BigIntegerField(primary_key=True)
    company_id_fk = models.IntegerField()
    payroll_schedule = models.IntegerField()
    autorun_schedule = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_payroll_schedule'


class RecordTraining(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField()
    training_id = models.IntegerField()
    note = models.CharField(max_length=250)
    date_training = models.DateField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_record_training'


class SalaryHistory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField()
    old_salary = models.IntegerField()
    new_salary = models.IntegerField()
    effective_date = models.DateField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_salary_history'


class StructurePattern(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    pattern_id = models.IntegerField()
    days = models.IntegerField()
    from_field = models.TimeField(db_column='from')  # Field renamed because it was a Python reserved word.
    from_format = models.IntegerField()
    to = models.TimeField()
    to_format = models.IntegerField()
    break_minutes = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_structure_pattern'


class TaskOnboarding(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    onboarding_id = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_task_onboarding'


class Tasks(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fk_ref = models.IntegerField()
    company_id = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.IntegerField()
    assigned_from = models.IntegerField()
    deadline = models.DateField()
    status_employee_tasks = models.IntegerField()
    status_tasks = models.IntegerField()
    type_task = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    delete_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tasks'


class TeamOnboarding(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField()
    organization_id = models.IntegerField()
    onboarding_id = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_team_onboarding'


class TempThr(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.IntegerField()
    user_id = models.IntegerField()
    thr = models.FloatField()
    annual_gross = models.FloatField()
    position_cost = models.FloatField()
    jht_employee_yearly = models.FloatField()
    netto_yearly = models.FloatField()
    ptkp = models.IntegerField()
    pkp = models.FloatField()
    pph_yearly = models.FloatField()
    pph_thr = models.FloatField()
    payment_date = models.DateField()
    religion_holiday = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_temp_thr'


class Thr(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.IntegerField()
    religion_holiday = models.CharField(max_length=20, blank=True)
    min_month = models.IntegerField()
    after_month = models.IntegerField()
    no_rounding = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_thr'


class ThrMultiplier(models.Model):
    multiplier_id = models.BigIntegerField(primary_key=True)
    company_id = models.BigIntegerField()
    joined_years = models.BigIntegerField()
    multiplier = models.BigIntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_thr_multiplier'


class ThrPayrollComponent(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.IntegerField()
    payroll_component_id = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_thr_payroll_component'


class TimeOff(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField()
    policy_id = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    total = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_time_off'


class TimeOffPolicies(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.IntegerField()
    policy_name = models.CharField(max_length=100)
    effectice_date = models.DateField()
    policy_flag = models.IntegerField()
    total_time_off = models.IntegerField(blank=True, null=True)
    renew_flag = models.IntegerField()
    renew_day = models.IntegerField(blank=True, null=True)
    renew_month = models.IntegerField(blank=True, null=True)
    expire_on = models.IntegerField()
    time_off_over_flag = models.IntegerField()
    time_off_over_date = models.IntegerField(blank=True, null=True)
    new_employee_request = models.IntegerField()
    time_off_over_days = models.IntegerField(blank=True, null=True)
    time_off_over_month = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_time_off_policies'


class TimeOffRequest(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.IntegerField()
    employee_id = models.IntegerField()
    available = models.IntegerField()
    requested = models.IntegerField()
    approved = models.IntegerField()
    approve_flag = models.IntegerField()
    taken = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    policy_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_time_off_request'


class TimeOffTaken(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField()
    timeoff_id = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    pic_id = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    company_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_time_off_taken'


class Title(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=50)
    company_id = models.IntegerField()
    level = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_title'


class ToolsOnboarding(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    onboarding_id = models.IntegerField()
    tool_name = models.CharField(max_length=150)
    login_url = models.CharField(max_length=250)
    description = models.TextField()
    file_url = models.CharField(max_length=150)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_tools_onboarding'


class Training(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.IntegerField()
    training_name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_training'


class User(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    company_id = models.IntegerField(blank=True, null=True)
    id_employee = models.CharField(max_length=20)
    citizen_id = models.CharField(max_length=200)
    barcode = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=225, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.IntegerField()
    job_id = models.IntegerField()
    organization_id = models.IntegerField()
    gender = models.IntegerField()
    birth_date = models.DateField(blank=True, null=True)
    birth_place = models.CharField(max_length=50, blank=True)
    address = models.TextField()
    city = models.CharField(max_length=50)
    religion = models.IntegerField(blank=True, null=True)
    marital_status = models.IntegerField()
    mobile_phone = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, blank=True)
    avatar = models.CharField(max_length=100, blank=True)
    salary = models.IntegerField()
    tax_config = models.IntegerField()
    tax_status = models.IntegerField()
    jkk_status = models.IntegerField()
    bank_name = models.IntegerField(blank=True, null=True)
    bank_account = models.CharField(max_length=255, blank=True)
    bank_account_holder = models.CharField(max_length=100, blank=True)
    npwp = models.CharField(max_length=200)
    bpjstk = models.CharField(max_length=200)
    bpjsk = models.CharField(max_length=200)
    status = models.IntegerField()
    status_employee = models.IntegerField()
    join_date = models.DateField()
    working_date = models.DateField(blank=True, null=True)
    end_contract_date = models.DateField()
    end_employee_date = models.DateField()
    end_probation_date = models.DateField()
    time_off_policies_id = models.IntegerField()
    role = models.IntegerField()
    last_login = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    pattern = models.IntegerField(blank=True, null=True)
    token = models.TextField(blank=True)
    onboarding_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user'
