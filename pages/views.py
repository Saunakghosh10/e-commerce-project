from django.shortcuts import render

navbar_context = {'uname':''}

# Create your views here.
def home_view(request):
	get_session(request)
	return render(request, "index.html", navbar_context)

def contact_view(request):
	get_session(request)
	return render(request, "contact.html", navbar_context)

# updating navbar context for navbar.html
def get_session(request):

	global navbar_context
	if 'user' in list(request.session.keys()):
		navbar_context['uname'] = dict(request.session.items())['user']
	else:
		navbar_context['uname'] = ''