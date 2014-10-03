from django.contrib import admin
from django_codecult.models import *
from django_summernote.admin import SummernoteModelAdmin

class AdminBlock(SummernoteModelAdmin):
	base_model = Block
 
class AdminPage(SummernoteModelAdmin):
	base_model = Page

class AdminIndex(SummernoteModelAdmin):
	base_model = Index

admin.site.register(Block, AdminBlock)
admin.site.register(Listblock)
admin.site.register(Page, AdminPage)
admin.site.register(Index, AdminIndex)
admin.site.register(Imageslider)
admin.site.register(Contactbuttons)


