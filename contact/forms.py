from django import forms
from .validators import validate_my_name

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100, validators=[validate_my_name])
	message = forms.CharField(required=True, error_messages={'required':'Please specify the message'})
	sender = forms.EmailField(widget = forms.EmailField.widget(attrs={'class':'contact_email'}), error_messages={'invalid':'Email provided is invalid'})
	cc_myself = forms.BooleanField(required=False)