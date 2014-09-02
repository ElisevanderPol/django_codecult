from django.db import models

class Top(models.Model):
    image = models.URLField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

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
	pro_con_list = models.BooleanField(default=False)
	third_party = models.BooleanField(default=False)
	href = "#" + str(title)

	def __repr__(self):
        return '%s' % (self.title)

    def __unicode__(self):
        return unicode(self.title)

class Page(models.Model):
	pass