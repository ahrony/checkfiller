from datetime import datetime
from django import forms
from crispy_forms.helper import FormHelper

from check.models import Checkdetails

class CheckDetailsForm(forms.ModelForm):
	name = forms.CharField(max_length=100)
	total_ammount = forms.DecimalField(max_digits=10, decimal_places=2)
	ammount_in_word = forms.CharField(max_length=100)
	date = forms.DateField()

	class Meta:
		model = Checkdetails
		
