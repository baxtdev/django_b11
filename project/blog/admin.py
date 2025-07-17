from django.contrib import admin

from .models import News,NewsImage,Category
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass