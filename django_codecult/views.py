from django.http import HttpResponse
from django.shortcuts import render
from django_codecult.models import *
from django.contrib.auth import authenticate, login

def home(request):
	page = Index.objects.all()
	block_list = page[0].blocks.all()
	return render(request, 'index.html', {
		'block_list': block_list,
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

def profile(request, user_name, message=None):
	user = User.objects.get(username=user_name)
	return render(request, 'profile.html', {
		'user': user,
		'message': message,
		})

def update_info(request):
	if(request.method=="POST"):
		first_name = request.POST.get('first_name', None)
		last_name = request.POST.get('last_name', None)
		email = request.POST.get('email', None)
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
		request.user.save()
	if(len(message) < 1):
		message.append("Alle velden zijn leeg.")
	return render(request, 'profile.html', {
		'user':request.user,
		'message':message
		})
