
from django.shortcuts import render, redirect
from .forms import TweetForm
from .models import Tweet

def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tweets:tweets')
    else:
        form = TweetForm()
    tweets = Tweet.objects.all()
    return render(request, 'tweet_create.html', {'form': form, 'Tweet': tweets})