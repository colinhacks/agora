from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from postapp.models import Post, Vote
from cityapp.models import City

def create_post(request, *args, **kwargs):
	return render(request, 'create_post.html',{'extension':'template.html'})

def create_comment(request, *args, **kwargs):
	return render(request, 'create_comment.html', {'extension':'template.html'})

def process_create_post(request, *args, **kwargs):
	if request.method == 'POST':
		import datetime
		post = Post(post_date=datetime.datetime.now(),title=request.POST['title'],content=request.POST['content'],user=request.user,city=City.objects.get(pk=1))
		post.save()
		#post = Post.objects.get(name=request.POST['post'])
    	#comment = Comment(post=post, content=request.POST['content'])
    	#comment.save()
    	return HttpResponseRedirect('/city/1')#render(request, 'post.html',{'post':post})
	return HttpResponseRedirect('/')



def process_create_comment(request, *args, **kwargs):
	if request.method == 'POST':
		import datetime
		post= Post(date=datetime.datetime.now(),title=request.POST['title'],content=request.POST['content'],user=request.user,city=City.objects.get(pk=1))
		post.save
		#post = Post.objects.get(name=request.POST['post'])
    	#comment = Comment(post=post, content=request.POST['content'])
    	#comment.save()
    	return HttpResponseRedirect('/city/1')#render(request, 'post.html',{'post':post})
	return HttpResponseRedirect('/')

def vote(request, *args, **kwargs):
	if request.is_ajax():
		user = request.user
		print "POST: ",request.POST
		pk = request.POST['post_pk']	
		print "test"	
		vote_value = request.POST['vote_status']
		print "test"	

		post = Post.objects.get(pk=pk)
		print "test"	
		post.score += int(vote_value)
		print "test"	
		post.save()
		print "test"	
		if vote_value == 1:
			test=True
		else:
			test=False
		print "test"	
		vote = Vote(user=user, post=post, vote=test)
		print "test"	
		vote.save()
		print "test"	
		return "Success"
	else:
		return "Error"
		


