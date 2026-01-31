from django import forms

from . models import Package

import os

class PackageForm(forms.ModelForm):


    class Meta:

        model = Package

        # fields = ['name','photo','description','start_date','destination_type','duration','package_type','mentor','price']

        # fields = '__all__'

        exclude = ['uuid','active_status']

        widgets = {

            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Package Name'}),

            'photo': forms.FileInput(attrs={'class':'form-control'}),

            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Package Description','rows':4}),

            'start_date': forms.DateInput(attrs={'class':'form-control','type':'date'}),

            'destination_type': forms.Select(attrs={'class':'form-select'}),

            'duration': forms.TextInput(attrs={'class':'form-control','placeholder':'e.g., 5 Days / 4 Nights'}),

            'package_type': forms.Select(attrs={'class':'form-select'}),

            'mentor': forms.SelectMultiple(attrs={'class':'form-select'}),

            'price': forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Package Price'}),

        }



    def clean_(self):

        cleaned_data = super().clean()

        print(cleaned_data)

        photo = cleaned_data.get('photo')

        if photo and photo.size > 3 * 1024 * 1024:  # 2MB limit

            self.add_error('photo', 'Image size should not exceed 3MB.')