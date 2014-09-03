from django.http import HttpResponse
from django.shortcuts import render
from django_codecult.models import *

def index(request):
	block_list = Block.objects.all()
	print block_list
	return render(request, 'index.html', {'blocks': block_list})