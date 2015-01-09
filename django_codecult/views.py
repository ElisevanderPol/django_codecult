from django.http import HttpResponse
from django.shortcuts import render
from django_codecult.models import *
from django.contrib.auth import authenticate, login

def home(request):
	pages = Page.objects.all()
	for page in pages:
		if page.home_page:
			block_list = page.blocks.all()
	try:
		return render(request, 'page.html', {
			'block_list': block_list,
			})
	except UnboundLocalError:
		return render(request, 'error.html', {
			'message': "No index page has been specified for this site! Please create one using Django admin.</p>"
			})

def info(request, page_title):
	page = Page.objects.get(title=page_title)
	block_list = page.blocks.all()
	block_list_tuples = []
	for i in range(0, len(block_list)):
		if(i%2 == 0 and i is not len(block_list)-1):
			block_list_tuples.append([block_list[i], block_list[i+1]])
		elif(i%2 == 0):
			block_list_tuples.append([block_list[i]])
	return render(request, 'page.html', {
		'page': page,
		'block_list': block_list,
		})

def change_profile(request, user_name):
	user = User.objects.get(username=user_name)
	profile = UserProfile.objects.get(user=user)
	languages = profile.languages.all()
	language_string = ""
	for language in languages:
		language_string += str(language) + ", "
	return render(request, 'change_profile.html',{
		'user': user,
		'profile': profile,
		'languages': language_string,
		})

def profile(request, user_name, message=None):
	user = User.objects.get(username=user_name)
	profile, created = UserProfile.objects.get_or_create(user=user)
	return render(request, 'profile.html', {
		'user': user,
		'message': message,
		'profile':profile,
		})

def update_info(request):
	if(request.method=="POST"):
		first_name = request.POST.get('first_name', None)
		last_name = request.POST.get('last_name', None)
		email = request.POST.get('email', None)
		about = request.POST.get('about', None)
		languages = request.POST.get('languages', None)
		profile = UserProfile.objects.get(user=request.user)
		message = []
		if(len(first_name) > 0):
			request.user.first_name = first_name
			message.append("<span class='field'>Voornaam</span> is veranderd naar <span class='value'>" + first_name + ".</span>")
		if(len(last_name) > 0):
			request.user.last_name = last_name
			message.append("<span class='field'>Achternaam</span> is veranderd naar <span class='value'>" + last_name + ".</span>")
		if(len(email) > 0):
			request.user.email = email
			message.append("<span class='field'>E-mail</span> is veranderd naar <span class='value'>" + email + ".</span>")
		if(len(about) > 0):
			request.user.about = about
			message.append("<span class='field'>Over mij</span> is veranderd naar <span class='value'>" + about + ".</span>")
		if(len(languages) > 0):
			languages = set(languages.split(","))
			language_list=""
			language_array =[]
			for lang in languages:
				lang = lang.strip().lower()
				if(lang not in language_array):
					language_array.append(lang)
					lang_obj,created = Language.objects.get_or_create(name=lang)
					profile.languages.add(lang_obj)
					profile.save()
					language_list += str(lang_obj.name) + ", "
			message.append("De volgende <span class='field'>programmeertalen</span> zijn toegevoegd: <span class'value'>" + str(language_list[:-2]) +".</span>")
		request.user.save()
	if(len(message) < 1):
		message.append("Alle velden zijn leeg.")
	return render(request, 'profile.html', {
		'user':request.user,
		'message':message,
		'profile':profile,
		})

def remove_language(request):
	if(request.method=="POST"):
		language = request.POST.get('language', None).strip().lower()
		profile = UserProfile.objects.get(user=request.user)
		lang_obj = Language.objects.get(name=language)
		profile.languages.remove(lang_obj)
	return render(request, 'profile.html', {
		'user': request.user,
		'message': "",
		'profile': profile,
		})
