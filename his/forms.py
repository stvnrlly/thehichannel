from django import forms
from his.models import Hi


class HiForm(forms.ModelForm):
    class Meta:
        model = Hi
        fields = ['message', 'sender']
        widgets = {
            'message': forms.TextInput(attrs={'class': 'form-control'})
        }
