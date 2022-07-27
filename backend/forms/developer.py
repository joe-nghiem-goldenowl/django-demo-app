from django import forms
from django.forms import ModelForm
from ..models import Developer
from django.utils.translation import gettext_lazy as _

class DeveloperForm(ModelForm):
    template_name = "forms/developer_form.html"
    class Meta:
        model = Developer
        fields = '__all__'
        labels = {
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'language': _('Language'),
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'col-10 form-control required',}),
            'last_name': forms.TextInput(attrs={'class': 'col-10 form-control required',}),
            'language': forms.Select(attrs={'class': 'col-10 form-control required',}),
        }