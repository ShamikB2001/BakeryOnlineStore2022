from django import forms
from bakery.models import itemdetails
from bakery.models import accountdb
from bakery.models import customerorderdetails
class userForm(forms.ModelForm):
	class Meta:
		model=itemdetails
		fields="__all__"
class cForm(forms.ModelForm):
	class Meta:
		model=accountdb
		fields="__all__"
class userForm2(forms.ModelForm):
	class Meta:
		model=customerorderdetails
		fields="__all__"