from django import forms
from .models import ReportProblemTable

class ReportProblemForm(forms.ModelForm):
    class Meta:
        model = ReportProblemTable
        fields = [
            'user_id',
            'problem_description',
            'serial_number',
            'status_indicator1',
            'status_indicator2',
            'status_indicator3'
        ]
        labels = {
            'user_id': 'User ID',
            'problem_description': 'Problem description',
            'serial_number': 'Serial number',
            'status_indicator1': 'Status Indicator 1',
            'status_indicator2': 'Status Indicator 2',
            'status_indicator3': 'Status Indicator 3'
        }