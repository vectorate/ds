from django.core.exceptions import ValidationError

def validate_my_name(value):
	if value != "moabi":
		raise ValidationError(u'%s is not moabi' % value)
