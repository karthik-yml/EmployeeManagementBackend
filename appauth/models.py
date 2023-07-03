from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _

from . constants import DEPARTMENT_CHOICES, PROJECT_CHOICES


class EmployeeUser(AbstractUser):
    city = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    state = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    department = models.CharField(max_length=100, blank=False, null=False)
    project_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.CharField(max_length=128, blank=False, null=False)
    date_of_joined = models.DateField()
    is_still_in_company = models.BooleanField(default=True)
    designation = models.CharField(max_length=100, blank=False, null=False)

    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    employee_id = models.CharField(max_length=20, unique=True, editable=False)
    
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES, blank=False, null=False)
    project_name = models.CharField(max_length=100, choices=PROJECT_CHOICES, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def save(self, *args, **kwargs):
        if not self.id:
            import ipdb; ipdb.set_trace()
            # Generate the employee_id when creating a new employee
            company_name = "COMPANY_NAME"  # Replace with your company name
            last_employee = EmployeeUser.objects.order_by('id').last()
            if last_employee:
                employee_id = f"{company_name}{str(last_employee.id + 1).zfill(4)}"
            else:
                employee_id = f"{company_name}0001"
            self.employee_id = employee_id

            self.username = f"{self.first_name} {self.last_name}"

        super().save(*args, **kwargs)

    # Add any other fields, methods, or meta options as needed
