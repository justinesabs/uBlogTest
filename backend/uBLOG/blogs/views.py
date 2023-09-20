from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Blog

# Create your views here.
def blogs(request):
    blogs = Blog.objects.all().order_by('date')
    return render(request, 'blogs/blogs.html', { 'blogs': blogs })

def blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blogs/blog.html', { 'blog': blog })
    # try:
    #     blogs = Blog.objects.all().order_by('date')
    #     for blog in blogs:
    #         if blog.author.username == author and blog.slug == slug: 
    #             return render(request, 'blogs/blog.html', { 'blog': blog })
    # except:
        # return redirect('blogs:blogs')

    

@login_required(login_url="/accounts/login/")
def create_blog(request):
    if request.method == 'POST':
        form = forms.CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blogs:blogs')
    else:
        form = forms.CreateBlog()
    return render(request, 'blogs/create.html', { 'form': form })

@login_required(login_url="/accounts/login/")
def update_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    if request.method == 'POST':
        form = forms.UpdateBlog(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')
    else:
        form = forms.UpdateBlog(instance=blog)
        print(blog.author)
    return render(request, 'blogs/update.html', {'blog': blog ,'form': form})

@login_required(login_url="/accounts/login/")
def delete_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    print(request)
    if request.method == 'GET':
        blog.delete()
        return redirect('blogs:blogs')