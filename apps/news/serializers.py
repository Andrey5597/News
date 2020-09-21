from django.db.models import F
from rest_framework import serializers

from apps.news import models


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(
        queryset=models.Post.objects.all(), write_only=True
    )

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'author_name',
            'content',
            'creation_date',
            'post',
        )


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = models.Post
        fields = (
            'id',
            'title',
            'link',
            'creation_date',
            'amount_of_upvotes',
            'author_name',
            'comments',
        )

    def get_comments(self, obj):
        return CommentSerializer(obj.post_comments, many=True).data


class UpvoteSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        self.instance.amount_of_upvotes = F('amount_of_upvotes') + 1
        self.instance.save()
        return instance
