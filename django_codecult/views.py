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

def profile(request, user_name):
	user = User.objects.get(username=user_name)
	return render(request, 'profile.html', {
		'user': user
		})

def update_info(request):
	if(request.method=="POST"):
		first_name = request.POST.get('first_name', None)
		last_name = request.POST.get('last_name', None)
		email = request.POST.get('email', None)
		if(len(first_name) > 0):
			request.user.first_name = first_name
		if(len(last_name) > 0):
			request.user.last_name = last_name
		if(len(email) > 0):
			request.user.email = email
		request.user.save()
