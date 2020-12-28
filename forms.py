from django import forms
from .models import assignments

class DocumentForm(forms.ModelForm):
    class Meta:
        model = assignments
        fields = ('Name','Branch','Subjects','Rollno','AssignmentName', 'file')