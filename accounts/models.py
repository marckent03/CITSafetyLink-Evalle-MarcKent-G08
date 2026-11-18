from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student/Faculty'),
        ('security', 'Security Office/Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    contact_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"