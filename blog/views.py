from django.shortcuts import render
from .models import post

# Create your views here.
def home (request):
	return render(request, 'home.html', locals())

def albums (request):
	return render(request, 'albums.html', locals())

def contacts (request):
	return render(request, 'contacts.html', locals())

def post_list (request):
	all_posts = post.objects.all
	return render(request, 'list.html', locals())

def post_detail (request, post_id = 1):
	some_post = post.objects.get(id = post_id)
	return render(request, 'post.html', locals())

