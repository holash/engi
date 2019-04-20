from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm, ReplyForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(date_posted__lte=timezone.now()).order_by('date_posted')
	return render(request, 'story/post_list.html',  {'posts': posts})

def about(request):
    return render(request, 'story/about.html',  {'title': 'About'})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'story/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_posted = timezone.now()
            post.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'story/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_posted = timezone.now()
            post.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'story/post_edit.html', {'form': form})

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'story/add_comment_to_post.html', {'form': form})

@login_required
def reply(request, pk, pk1):
    #comment = get_object_or_404(Post, pk=pk)
    comment = get_object_or_404(Comment, pk=pk1)
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = comment
            reply.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = ReplyForm()
    return render(request, 'story/reply.html', {'form': form})