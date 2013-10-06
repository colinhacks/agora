from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

def file_name(instance, filename):
    return 'postpics/'+instance.pk+"/profile.jpg"

class Post(models.Model):
	post_date = models.DateTimeField(auto_now_add=True, null=True,blank=True)
	title = models.CharField(max_length=100,default="Title")
	city = models.ForeignKey('cityapp.City',related_name='posts')
	user = models.ForeignKey(User,related_name='posts')
	score = models.IntegerField(default=0)
	picture = models.ImageField(upload_to=file_name, max_length=200, blank=True, null=True)
	resolved = models.BooleanField(default=False) 
	content = models.TextField(max_length=1000, blank=False, null=False)

	def __unicode__(self):
		return self.title
	
class Vote(models.Model):
	post = models.ForeignKey(Post,related_name='votes')
	user = models.ForeignKey(User,related_name='votes')
	vote = models.BooleanField()
	def __unicode__(self):
		if self.vote:
			return self.user.first_name+" upvoted "+self.post.title
		else:
			return self.user.first_name+" downvoted "+self.post.title

class Comment(models.Model):
	post = models.ForeignKey(Post,related_name='comments')
	content = models.TextField(max_length=1000, blank=False, null=False)
	def __unicode__(self):
		return self.content

admin.site.register(Comment)
admin.site.register(Vote)
admin.site.register(Post)