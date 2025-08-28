from django.contrib import admin
from django.utils.safestring import mark_safe


from .models import News,NewsImage,Category,Tag
# Register your models here.



class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 0



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','description','is_published','views','get_image']
    readonly_fields = ['get_image']
    inlines = [NewsImageInline]

    @admin.display(description='Изображение')
    def get_image(self, news):
        return mark_safe(f'<img src={news.image.image.url if news.image else "-"} width="150px" />')


@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    list_display = ['news__title','get_image']

    @admin.display(description='Изображение')
    def get_image(self, news):
        return mark_safe(f'<img src={news.image.url if news.image else "-"} width="150px" />')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass