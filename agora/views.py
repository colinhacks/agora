from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from postapp.models import Post,Comment
from cityapp.models import City



def home(request, *args, **kwargs):
	return render(request, kwargs['template'],{'extension':'template.html'})

def thread(request, *args, **kwargs):
	post = Post.objects.get(pk=kwargs['pk'])
	time = post.post_date.strftime("%b %e, %l:%M %p")
	#time ="November 12, 2012"
	comments = Comment.objects.filter(post=post)
	num_comments = post.comments.count()
	return render(request, kwargs['template'],{'comments':comments,'num_comments':num_comments,'time':time,'post':post,'extension':'template.html'})

def city(request, *args, **kwargs):
	
	posts_time = Post.objects.order_by('score')

	return render(request, kwargs['template'],{'extension':'template.html'})

def allposts(request, *args, **kwargs):
	city = City.objects.get(pk=kwargs['pk'])
	num_users = city.residents.count()
	posts = Post.objects.order_by('score')[:10]
	num_posts = city.posts.count()
	return render(request, kwargs['template'],{'posts':posts,'city':city,'num_users':num_users,'num_posts':num_posts,'extension':'template.html'})

@login_required
def hello(request, **kwargs):
	return HttpResponse("Welcome, "+request.user.username+"!<br /><a href='/logout'>Logout</a>")

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def login(request, **kwargs):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/city/1')
	if request.method == "POST":
		username=request.POST['username']
		password=request.POST['password']
		user = auth.authenticate(username=username, password=password)
		auth.login(request, user)
		return HttpResponseRedirect('/city/1')
	else:
		return render(request, kwargs['template'],{'extension':'template.html'})
