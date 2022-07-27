from django.forms import ModelForm
from ..models import Developer, Project
from django import forms
from django.utils.translation import gettext_lazy as _
class ProjectForm(ModelForm):
    template_name = "forms/project_form.html"
    class Meta:
        model = Project
        fields = '__all__'
        labels = {
            'name': _("Name"),
            'description': _("Description"),
            'cost': _("Cost"),
            'date_start': _("Date start"),
            'date_end': _("Date end"),
            'developer': _("Developer"),
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-10 form-control required',}),
            'description': forms.TextInput(attrs={'class': 'col-10 form-control required',}),
            'cost': forms.NumberInput(attrs={'class': 'col-10 form-control required',}),
            'date_start': forms.DateInput(attrs={'class': 'col-10 form-control required', 'type': 'date'}),
            'date_end': forms.DateInput(attrs={'class': 'col-10 form-control required', 'type': 'date'}),
            'developer': forms.Select(attrs={'class': 'col-10 form-control required',})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['developer'].queryset = Developer.objects.filter(project=None)
    
    def clean_date_end(self):
        date_start = self.cleaned_data['date_start']
        date_end = self.cleaned_data['date_end']

        if date_end < date_start:
            raise forms.ValidationError(_("Start date must be earlier than end date"))
        
        return date_end