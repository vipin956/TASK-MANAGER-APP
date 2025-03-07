from django import forms
from tasks.models import TASK

class TASKFORM(forms.ModelForm):
    class Meta:
        model = TASK
        fields = '__all__'