from django import forms

from . models import Package

import os

class PackageForm(forms.ModelForm):

    class Meta:

        model = Package

        exclude = ['uuid', 'active_status']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),

            'photo': forms.FileInput(attrs={'class':'form-control'}),

            'description': forms.Textarea(attrs={'class':'form-control','rows':4}),

            'start_date': forms.DateInput(attrs={'class':'form-control','type':'date'}),

            'destination_type': forms.Select(attrs={'class':'form-select'}),

            'duration': forms.TextInput(attrs={'class':'form-control'}),

            'package_type': forms.Select(attrs={'class':'form-select'}),

            'mentor': forms.Select(attrs={'class':'form-select'}),  

            'price': forms.NumberInput(attrs={'class':'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        photo = cleaned_data.get('photo')

        if photo and photo.size > 3 * 1024 * 1024:
            
            self.add_error('photo', 'Image size should not exceed 3MB.')

        return cleaned_data
