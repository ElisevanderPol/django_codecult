from django.http import HttpResponse
from django.shortcuts import render
from django_codecult.models import *
from django.contrib.auth import authenticate, login

def home(request):
	page_list = Page.objects.all()
	page = Index.objects.all()
	block_list = page[0].blocks.all()
	return render(request, 'index.html', {
		'pages': page_list,
		'block_list': block_list,
		})

def info(request, page_title):
	page_list = Page.objects.all()
	page = Page.objects.get(title=page_title)
	block_list = page.blocks.all()
	block_list_tuples = []
	for i in range(0, len(block_list)):
		if(i%2 == 0 and i is not len(block_list)-1):
			block_list_tuples.append([block_list[i], block_list[i+1]])
		elif(i%2 == 0):
			block_list_tuples.append([block_list[i]])
	return render(request, 'page.html', {
		'pages': page_list,
		'page': page,
		'block_list': block_list,
		})

def user_login(request):
	state = "Meld je aan.."
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			state = "Welkom terug bij CodeCult!"
		else:
			state = "Deze gebruiker is niet actief."
	else:
		state = "Deze gebruikersnaam/wachtwoord-combinatie is niet geldig."

	return render(request, 'index.html', {
	'state':state, 
	'username': username
	})	