from rest_framework import serializers

from blog.models import News,Category,Tag,NewsImage



class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']



class NewsSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # category = CategorySerializer(read_only=True,required=False)
    # tag = TagSerializer(many=True,required=False)
    # images = NewsImageSerializer(many=True,required=False)
    class Meta:
        model = News
        fields = '__all__'
    
    def create(self, validated_data):
        return super().create(validated_data)

    
    