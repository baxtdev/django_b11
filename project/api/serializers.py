from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from blog.models import News,Category,Tag,NewsImage
from accounts.models import CustomUser



class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # category = CategorySerializer(read_only=True,required=False)
    # tag = TagSerializer(many=True,required=False)
    # images = NewsImageSerializer(many=True,required=False)
    class Meta:
        model = News
        # fields = '__all__'
        exclude = ['category'] 
    
    def create(self, validated_data):
        return super().create(validated_data)


class CategorySerializer(WritableNestedModelSerializer):
    news = NewsSerializer(many=True)
    
    class Meta:
        model = Category
        fields = ['id','title','news']
    
    def create(self, validated_data):
        news = validated_data.pop('news',[])
        category = super().create(validated_data)
      
        for i in news:
            category.news.create(**i)

       
        return category


      # news_items = [News(category=category,**item) for item in news]
        # print(news_items)
        # news = News.objects.bulk_create(news_items)



from django.contrib.auth.password_validation import validate_password

    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        validators=[validate_password],
        write_only=True
        )
    class Meta:
        model = CustomUser
        exclude = ['groups','user_permissions',
                   'date_joined','is_active','is_staff',
                   'is_superuser','last_login']


    
    def create(self, validated_data):
        password = validated_data.get('password')
        user:CustomUser =  super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
