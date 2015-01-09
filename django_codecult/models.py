from django.db import models
from django.contrib.auth.models import User

class FancyUrl(models.Model):
	name = models.CharField(max_length=50, unique=True)
	url_string = models.URLField(max_length=255)

	font_awesome_id = models.CharField(max_length=50)

	def __repr__(self):
		return '%s' % (self.name)

	def __unicode__(self):
		return unicode(self.name)	

class Language(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __repr__(self):
		capitalized_name = self.name[0].upper()+self.name[1:]
		return '%s' % (capitalized_name)

	def __unicode__(self):
		capitalized_name = self.name[0].upper()+self.name[1:]
		return unicode(capitalized_name)

class TeaserImage(models.Model):
	name = models.CharField(null=True, max_length=255)
	image_url = models.URLField(null=True, max_length=255, blank=True)
	teaser_text = models.TextField(null=True, blank=True)

	def __repr__(self):
		return '%s' % (self.name)

	def __unicode__(self):
		return unicode(self.name)

class ImageTeaser(models.Model):
	name = models.CharField(null=True, max_length=255)
	images_list = models.ManyToManyField(TeaserImage)

	def get_teaser_images(self):
		return self.images_list.all()

	def __repr__(self):
		return '%s' % (self.name)

	def __unicode__(self):
		return unicode(self.name)

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    languages = models.ManyToManyField('Language', blank=True, related_name='users')
    profile_image = models.URLField(null=True, max_length=255, blank=True)

    def get_image_url(self):
    	return self.profile_image

class Listblock(models.Model):
	title = models.CharField(null=True, max_length=255)
	pro = models.TextField(null=True, blank=True)
	con = models.TextField(null=True, blank=True)

	def get_pro_list(self):
		return self.pro.split(',')

	def get_con_list(self):
		return self.con.split(',')
		
	def __repr__(self):
		return '%s' % (self.title)

	def __unicode__(self):
		return unicode(self.title)

class Contactbuttons(models.Model):
	title = models.CharField(null=True, max_length=255)
	facebook = models.URLField(null=True, max_length=255, blank=True)
	twitter = models.URLField(null=True, max_length=255, blank=True)
	gplus = models.URLField(null=True, max_length=255, blank=True)
	mail = models.EmailField(null=True, max_length=255, blank=True)
	
	def __repr__(self):
		return '%s' % (self.title)

	def __unicode__(self):
		return unicode(self.title)	

class Imageslider(models.Model):
	title = models.CharField(null=True, max_length=255)
	images = models.ManyToManyField(TeaserImage)
	show_teasers = models.BooleanField(default=False)

	def get_image_urls(self):
		all_images = self.images.all()
		urls_list = []
		for image in all_images:
			urls_list.append(image.image_url)
		return urls_list
		
	def __repr__(self):
		return '%s' % (self.title)

	def __unicode__(self):
		return unicode(self.title)		

class Block(models.Model):
	image = models.URLField(max_length=255, null=True, blank=True)
	title = models.CharField(max_length=255)
	display_title = models.BooleanField(default=True)
	description = models.TextField(null=True, blank=True)
	#form = models.BooleanField(default=False)
	#third_party = models.BooleanField(default=False)
	href = "#" + str(title)
	pro_con_list = models.ForeignKey(Listblock, blank=True, null=True)
	image_slider = models.ForeignKey(Imageslider, blank=True, null=True)
	contact_buttons = models.ForeignKey(Contactbuttons, blank=True, null=True)
	image_teaser = models.ForeignKey(ImageTeaser, blank=True, null=True)
	fancy_url = models.ManyToManyField(FancyUrl, blank=True, null=True)

	def get_fancy_urls(self):
		return self.fancy_url.all()

	def __repr__(self):
		return '%s' % (self.title)

	def __unicode__(self):
		return unicode(self.title)

class Page(models.Model):
	title = models.CharField(max_length=255, unique=True)
	blocks = models.ManyToManyField(Block)
	home_page = models.BooleanField(default=False)

	def __repr__(self):
		return '%s' % (self.title)

	def __unicode__(self):
		return unicode(self.title)		