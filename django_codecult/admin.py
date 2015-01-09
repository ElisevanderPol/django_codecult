from django.contrib import admin
from django_codecult.models import *
from django_summernote.admin import SummernoteModelAdmin

class AdminBlock(SummernoteModelAdmin):
	base_model = Block
 
class AdminPage(SummernoteModelAdmin):
	base_model = Page

admin.site.register(Block, AdminBlock)
admin.site.register(Listblock)
admin.site.register(Page, AdminPage)
admin.site.register(Imageslider)
admin.site.register(Contactbuttons)
admin.site.register(UserProfile)
admin.site.register(Language)
admin.site.register(ImageTeaser)
admin.site.register(FancyUrl)
admin.site.register(TeaserImage)
admin.site.register(UserDisplay)


