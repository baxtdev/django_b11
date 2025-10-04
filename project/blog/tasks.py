from celery import shared_task

from .models import News,Category
import time




@shared_task
def count_news_at_category():
    categories = Category.objects.all().prefetch_related('news')
    string_data = """"""


    for cat in categories:
        string_data+=f"Название:{cat.title} Кол-во новостей:{cat.news.count()}\n"
        time.sleep(1)
            
    with open("/Users/macpro2019/django_b11/report.txt","w") as file:
        file.write(string_data)

    print(string_data)
    return "Succes"









