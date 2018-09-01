from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect,redirect,Http404
from .models import Post
from .forms import PostForm,CommentForm
from django.contrib import messages
from django.urls import NoReverseMatch
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from contact.forms import ContactForm
from urllib.parse import quote_plus
from django.contrib.auth.decorators import login_required

def post_index( request ):
    post_list = Post.objects.all()

    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(Q(title__icontains = query) |
                                     Q(content__icontains = query) |
                                     Q(user__username__icontains = query)|
                                     Q (user__last_name__icontains=query)
                                     ).distinct()


    paginator = Paginator (post_list, 5)  # Show 25 contacts per page

    page = request.GET.get ('page')
    try:
        posts = paginator.page (page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page (1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page (paginator.num_pages)
    return render (request, 'post/index.html', {'posts': posts})


def post_detail( request, slug ):
    post = get_object_or_404 (Post, slug=slug)
    share_string = quote_plus(post.content)

    form = CommentForm (request.POST or None)
    if form.is_valid ():
        comment = form.save (commit=False)
        comment.post = post

        comment.save ()
        return HttpResponseRedirect (post.get_absolute_url())

    context = {
        'post': post,
        'form': form,
        'share_string': share_string,
    }
    return render (request, 'post/detail.html', context, )


def post_create( request ):
    if not request.user.is_authenticated:
        return Http404()
    form = PostForm ()

    # if request.method == "POST":
    # formdan gelen bilgileri kaydet
    # form = PostForm(request.POST)
    # if form.is_valid():
    # form.save()

    # else:

    # form =PostForm()

    form = PostForm (request.POST or None, request.FILES or None)
    if form.is_valid ():
        post = form.save(commit=False)
        post.user = request.user

        post.slug =slugify(post.title.replace('ı','i'))
        post.save()
        messages.success(request, 'Gönderi Kaydedildi')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }

    return render (request, 'post/form.html', context, )


def post_update( request, slug ):
    if not request.user.is_authenticated:
        return Http404()
    post = get_object_or_404 (Post, slug=slug)
    form = PostForm (request.POST or None, request.FILES or None, instance=post)
    if form.is_valid ():
        form.save ()
        messages.success(request, 'Gönderi Güncellendi')
        return HttpResponseRedirect (post.get_absolute_url())

    context = {'form': form}

    return render (request, 'post/form.html', context, )


def post_delete( request,slug ):
    if not request.user.is_authenticated:
        return Http404()
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'Gönderi başarıyla silindi')

    return redirect('post:index')


def about(request):
    return render(request,"aboutme.html",{})

def contact(request):

    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"Mesaj başarıyla gönderildi.")
        return redirect ('post:index')
    return render (request, "contact.html", {"form": form}, )