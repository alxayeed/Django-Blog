from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post 

# def home(request):
# 	context = {
# 	 'posts':Post.objects.all()
# 	}
# 	return render(request,'blog/home.html',context)

class PostListView(ListView):
	model = Post #The Model it will work on
	template_name = 'blog/home.html' #overriding default template name to search
	context_object_name = 'posts' #context with model objects
	ordering = ['-date_posted'] #ordering newest ot oldest

class PostDetailsView(DetailView):
	model = Post 
	

def about(request):
	return render(request,'blog/about.html',{'title':'About'})





