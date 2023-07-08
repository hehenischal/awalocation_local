from django.shortcuts import render,redirect,HttpResponse
from .models import Blog,Description
from .forms import BlogForm

# Create your views here.
def home(request):
    template_name = 'home.html'
    allblogs= Blog.objects.all()
    print(allblogs)
    context = {
        'blogs':allblogs,
    }
    return render(request,template_name,context)


def blog(request,blog_id):
    oneblog=Blog.objects.get(id=blog_id)
    print(oneblog)
    template_name = 'blog.html'
    context = {
        'blog':oneblog,
    }
    return render(request,template_name,context)

def createblog(request):
    if request.method == 'POST':
        title = request.POST['title']
        location = request.POST['location']
        things_to_do = request.POST['things_to_do']
        best_time_to_visit = request.POST['best_time_to_visit']
        unique_features = request.POST['unique_features']
        category = request.POST['category']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        image = request.FILES['image']
        author_name = request.user
        author_id=request.user.id
        desc = Description.objects.create(things_to_do=things_to_do,best_time_to_visit=best_time_to_visit,unique_features=unique_features)
        blog = Blog.objects.create(title=title,location=location,desc=desc,category=category,latitude=latitude,longitude=longitude,author_id=author_id,image=image,author_name=author_name)
        blog.save()
        return redirect('home')
    else:
        form = BlogForm()
    
        return render(request, 'createblog.html', {'form': form})

def searchblog(request,query):
    template_name = 'searchblog.html'
    allblogs= Blog.objects.filter(location__icontains=query,title__icontains=query)
    context = {
        'query':query,
        'blogs':allblogs,
    }
    return render(request,template_name,context)

def deleteblog(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    if(blog.author_name == request.user):
        blog.delete()
    return redirect('home')

def category(request,query):
    template_name = 'home.html'
    allblogs= Blog.objects.filter(category__icontains=query)
    context = {
        'query':query,
        'blogs':allblogs,
    }
    return render(request,template_name,context)

