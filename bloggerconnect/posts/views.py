from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReviewForm
from .models import Tag, Post
from .utils import searchPosts, paginatePosts


def posts(request):
    posts, search_query = searchPosts(request)
    custom_range, posts = paginatePosts(request, posts, 6)
    context = {'posts': posts, 'search_query': search_query,
               'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)


def post(request, pk):
    postObj = Post.objects.get(id=pk)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.post = postObj
        review.owner = request.user.profile
        review.save()
        postObj.getVoteCount
        messages.success(request, "Your review was successfully submitted!")
        return redirect('post', pk=postObj.id)
    return render(request, "projects/single-project.html", {"post": postObj, "form": form})
