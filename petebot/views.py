""" Cornice services.
"""
from cornice import Service
import re


hello = Service(name='hello', path='/', description="Simplest app")


@hello.get()
def get_info(request):
    """Returns Hello in JSON."""
    return {'Hello': 'World'}

@hello.post()
def hello_post(request):
	print request.POST
	if re.search('botsnack',request.POST['text']):
		return {'text': ':)' }
