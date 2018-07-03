from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.utils.text import slugify

def post_index(request):
    posts=Post.objects.all()
    return render(request, 'post/index.html',{'posts':posts})


def post_detail(request,slug):
    post = get_object_or_404(Post,slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'post/detail.html',context)

def post_create(request):

    if not request.user.is_authenticated():
        return Http404()



    #if request.method=="POST":
    #    print(request.POST)

    #title = request.POST.get('title')
    #content = request.POST.get('content')
    #Post.objects.create(title=title,content=content)

    #if request.method == "POST":
        #Formdan gelen bilgileri kaydet
        #form = PostForm(request.POST)
        #if form.is_valid():
            #form.save()
    #else:
        #formu kullanıcıya göster
        #form = PostForm()

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save()

        messages.success(request, 'Başarılı bir şekilde oluşturdunuz :')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form':form,
        }


    return render(request,'post/form.html',context)


def post_update(request,slug):
    if not request.user.is_authenticated():
        return Http404()
    post = get_object_or_404(Post,slug=slug)
    form = PostForm(request.POST or None, request.FILES or None , instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz :')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form':form,
    }

    return render(request,'post/form.html',context)


def post_delete(request,slug):
    if not request.user.is_authenticated():
        return Http404()
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('post:index')























# Create your views here.
