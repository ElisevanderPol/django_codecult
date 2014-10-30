from django.http import HttpResponse
from django.shortcuts import render
from django_codecult.models import *
from django.contrib.auth import authenticate, login

def menu_items(self):
	page_list = Page.objects.all()
	return {'pages': page_list,}