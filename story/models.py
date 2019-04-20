from django.conf import settings
from django.db import models
from django.utils import timezone
from PIL import Image


class Post(models.Model):
	SUCCESS_STORY = 'SUCCESS STORY'
	FUNDING = 'FUNDING'
	STARTUP = 'STARTUP'
	WOMEN = 'WOMEN'
	TECH = 'TECH'
	ART = 'ART AND CULTURE'
	my_category = (
		(SUCCESS_STORY,'SUCCESS STORY'),
		(FUNDING,'FUNDING'),
		(STARTUP,'STARTUP'),
		(WOMEN,'WOMEN ENTERPRENEURS'),
		(TECH,'TECH'),
		(ART,'ART AND CULTURE')
	)
	category = models.CharField(
        max_length=100,
        choices=my_category,
        default=SUCCESS_STORY,
    )
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	photo_post = models.ImageField(default='default.jpg',upload_to='post_pics/')

	def publish(self, *args , **kwargs):
		self.published_date = timezone.now()
		super().save()

		img = Image.open(self.photo_post.path)
		img.save(self.photo_post.path)

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey('story.Post', on_delete=models.CASCADE, related_name='comments')
	author = models.CharField(max_length=200)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)

	def approve(self):
		self.save()

	def __str__(self):
		return self.content

class Reply(models.Model):
	comment = models.ForeignKey('story.Comment', on_delete=models.CASCADE, related_name='reply')
	author = models.CharField(max_length=200)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)

	def approve(self):
		self.save()

	def __str__(self):
		return self.content