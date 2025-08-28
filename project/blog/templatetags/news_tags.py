from django import template

from blog.models import Category,News

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()

