from django.conf import settings
from django.db import models
# Create your models here.

STATUS_CHOICES = [
    ('applied', 'Applied'),
    ('interviewing', 'Interviewing'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
]


class JobApplication(models.Model):
    job_title = models.CharField(max_length=40)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.CharField(max_length=40)
    job_link = models.URLField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default='applied')
    date_applied = models.DateField(auto_now_add=True)
    notes = models.TextField()