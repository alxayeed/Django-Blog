from django.shortcuts import render

posts = [
	{
		'author':'Al Xayeed',
		'title': 'Post 1',
		'content':'Dummy data',
		'date':'November 17,2019'
	},
	{
		'author':'Ashiq Anik',
		'title': 'Post 2',
		'content':'Ha Ha Ho Ho',
		'date':'November 17,2019'
	}
]

def home(request):
	context = {
	 'posts':posts
	}
	return render(request,'blog/home.html',context)

def about(request):
	return render(request,'blog/about.html',{'title':'About'})



