from django.shortcuts import render

from .models import News
# Create your views here.

def news_list(request):
    news = News.objects.all()
    context = {
        'news':news
    }
    return render(request,'blog/news.html',context=context)