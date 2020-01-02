from django.db import models


class Employee(models.Model):
    uuid = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)


class Expense(models.Model):
    uuid = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(db_index=True)
    amount = models.IntegerField(db_index=True)
    currency = models.CharField(max_length=50)
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.IntegerField(db_index=True, default=0)
    employee_uuid = models.CharField(max_length=100)
    employee_first_name = models.CharField(max_length=100, null=True)
    employee_last_name = models.CharField(max_length=100, null=True)
