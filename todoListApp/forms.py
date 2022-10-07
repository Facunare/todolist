



from django.forms import Form, ModelForm, forms
from . import models
from django import forms

class createTasksForm(ModelForm):
    
    class Meta:
        model = models.taskForm
        fields = ['task_name']
        widgets = {
            'task_name': forms.TextInput(attrs={'placeholder': 'Type here to add tasks...'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
              