from django.db import models

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

class Block(models.Model):
	image = models.URLField(max_length=255, null=True, blank=True)
	title = models.CharField(max_length=255)
	description = models.TextField(null=True, blank=True)
	form = models.BooleanField(default=False)
	image_slider = models.BooleanField(default=False)
	third_party = models.BooleanField(default=False)
	href = "#" + str(title)
	pro_con_list = models.ForeignKey(Listblock, blank=True, null=True)

	def __repr__(self):
		return '%s' % (self.title)

	def __unicode__(self):
		return unicode(self.title)

class Page(models.Model):
	title = models.CharField(max_length=255, unique=True)
	blocks = models.ManyToManyField(Block)

	def __repr__(self):
		return '%s' % (self.title)

	def __unicode__(self):
		return unicode(self.title)

class Index(models.Model):
	blocks = models.ManyToManyField(Block)

	def __repr__(self):
		return '%s' % ("index")

	def __unicode__(self):
		return unicode("index")		