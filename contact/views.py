from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm

def contact(request):
	if request.method == 'POST': # If the form has been submitted...
		form = ContactForm(request.POST) # A form bound to the POST data

		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']
			
			recipients = ['moabi@ymail.com']
			
			if cc_myself:
				recipients.append(sender)

			from django.core.mail import send_mail
			send_mail(subject, message, sender, recipients)
			return HttpResponseRedirect('thanks/') # Redirect after POST

		else:
			#form = ContactForm(auto_id="%") # An unbound form
			return render(request, 'contact/contact.html', {
				'form': form,
			})
	else:
		form = ContactForm(auto_id="%") # An unbound form
		return render(request, 'contact/contact.html', {
			'form': form,
		})

def thanks(request):
	return render(request, 'contact/thanks.html')