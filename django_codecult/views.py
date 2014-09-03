from django.http import HttpResponse
from django.shortcuts import render
from django_codecult.models import *

def home(request):
	page_list = Page.objects.all()
	return render(request, 'index.html', {'pages': page_list})

def info(request, page_title):
	page_list = Page.objects.all()
	page = Page.objects.get(title=page_title)
	return render(request, 'page.html', {
		'pages': page_list,
		'page': page,
		'blocks': page.blocks.all(),
		})