from django import forms

class UploadForm(forms.Form):
	
	Image= forms.ImageField()
