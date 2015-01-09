from django.http import HttpResponse
from django.shortcuts import render
from django_codecult.models import *
from django.contrib.auth import authenticate, login

def menu_items(self):
	page_list = Page.objects.all()
	page_list = page_list.exclude(home_page=True)
	return {'pages': page_list,}