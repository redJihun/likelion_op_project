from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import BlogPost

# Create your views here.

def blogpost(request):
    if request.method=='POST':
        form=BlogPost(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form=BlogPost()
        return render(request,'new.html',{'form':form})

def home(request):
    blogs = Blog.objects
    blog_list=Blog.objects.all()
    paginator=Paginator(blog_list,2)
    page=request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request,'home.html',{'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})


def delete(request,blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id).delete()
    return redirect('home')

