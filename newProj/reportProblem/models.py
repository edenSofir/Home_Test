from django.db import models
from django.utils import timezone


INDICATOR_OPTIONS = [
    ("on","on"),
    ("off","off"),
    ("blinking","blinking")
]

class ReportProblemTable(models.Model):
    user_id = models.IntegerField()
    problem_description = models.TextField(max_length=300)
    serial_number = models.CharField(max_length=64)
    status_indicator1 = models.CharField(max_length=10,choices=INDICATOR_OPTIONS)
    status_indicator2 = models.CharField(max_length=10,choices=INDICATOR_OPTIONS)
    status_indicator3 = models.CharField(max_length=10,choices=INDICATOR_OPTIONS)
    response_status = models.CharField(max_length=300,blank=True,null=True)
    date_time = models.DateTimeField(default=timezone.now,blank=True)
