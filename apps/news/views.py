from rest_framework import viewsets, views

from . import models, serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.order_by('creation_date')
    serializer_class = serializers.PostSerializer

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return serializers.UpvoteSerializer
        return serializers.PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.order_by('creation_date')
    serializer_class = serializers.CommentSerializer


