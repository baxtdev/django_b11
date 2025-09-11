from rest_framework import serializers

from blog.models import News,Category,Tag


class NewsSerializer(serializers.Serializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        required = True
    )
    tag =  serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        required = False
    )
    title = serializers.CharField(required = True)
    description = serializers.CharField(required = False)
    date = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    views = serializers.IntegerField(read_only=True)
    is_published = serializers.BooleanField(required = False)
    
    def create(self, validated_data):
        tag = validated_data.pop('tag')
    
        news = News.objects.create(
            **validated_data
        )
        news.tag.set(tag)
        return news

    def update(self, instance:News, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.save()

        return instance