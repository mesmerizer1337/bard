from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ForumThread, ForumPost

def forum_list(request):
    """Displays a list of all forum threads"""
    threads = ForumThread.objects.all().order_by("-created_at")
    return render(request, "forums/forum_list.html", {"threads": threads})

def forum_thread(request, thread_id):
    """Displays a specific thread with its posts"""
    thread = get_object_or_404(ForumThread, id=thread_id)
    posts = thread.posts.all().order_by("created_at")  # All posts in the thread
    return render(request, "forums/forum_thread.html", {"thread": thread, "posts": posts})

@login_required
def create_thread(request):
    """Creates a new forum thread"""
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if not title:
            messages.error(request, "Thread title cannot be empty.")
            return render(request, "forums/create_thread.html")

        thread = ForumThread.objects.create(title=title)
        messages.success(request, "Thread created successfully!")
        return redirect("forum_list")

    return render(request, "forums/create_thread.html")

@login_required
def create_post(request, thread_id):
    """Creates a new post in a thread"""
    thread = get_object_or_404(ForumThread, id=thread_id)

    if request.method == "POST":
        content = request.POST.get("content", "").strip()
        if not content:
            messages.error(request, "Post content cannot be empty.")
            return render(request, "forums/create_post.html", {"thread": thread})

        ForumPost.objects.create(thread=thread, author=request.user, content=content)
        messages.success(request, "Post added successfully!")
        return redirect("forum_thread", thread_id=thread.id)

    return render(request, "forums/create_post.html", {"thread": thread})
