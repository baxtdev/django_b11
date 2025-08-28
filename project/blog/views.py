from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from .models import News, Category,Tag

@login_required
def news_list(request):
    news = News.objects.filter(is_published=True)
    categories = Category.objects.all()

    search = request.GET.get('search', '')
    category_id = request.GET.get('category', '')

    if search:
        news = news.filter(title__icontains=search)  

    if category_id:
        try:
            category = Category.objects.get(id=int(category_id))
            news = news.filter(category=category)
        except (Category.DoesNotExist, ValueError):
            category = None
    else:
        category = None

    context = {
        'news': news,
        'categories': categories,
        'search': search,
        'selected_category': category,
    }
    return render(request, 'blog/news.html', context)


# def news_list(request):
#     news = News.objects.filter(is_published=True)\
#         .select_related('category')\
#         .prefetch_related('images', 'tag')

#     categories = Category.objects.all()

#     return render(request, 'blog/news.html', {
#         'news': news,
#         'categories': categories
#     })


def news_detail(request, id):
    news = get_object_or_404(News.objects.prefetch_related('images', 'tag'), id=id)

    news.views += 1
    news.save(update_fields=['views'])

    return render(request, 'blog/news_detail.html', {
        'news': news,
        'categories': Category.objects.all(),  # для хедера
    })


def news_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    news_list = News.objects.filter(category=category, is_published=True)\
        .select_related('category')\
        .prefetch_related('images', 'tag')

    return render(request, 'blog/news.html', {
        'news': news_list,
        'categories': Category.objects.all(),
        'selected_category': category
    })




def news_create(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        tag_ids = request.POST.getlist('tags')
        images = request.FILES.getlist('images')

        category = Category.objects.get(id=category_id)

        news = News.objects.create(
            title=title,
            description=description,
            category=category,
            author=request.user,
        )
        news.tag.set(tag_ids)
        for image in images:
            news.images.create(
                image=image
            )

        return redirect('news-detail', news.id)

    return render(request, 'blog/news_create.html', {
        'categories': categories,
        'tags': tags
    })
