from rest_framework import viewsets

from . import models, serializers


class PostViewSet(viewsets.ModelViewSet):
    """ CRUD for Post entity + PATCH for increase amount_upvote counter"""
    queryset = models.Post.objects.order_by('creation_date')
    serializer_class = serializers.PostSerializer

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return serializers.UpvoteSerializer
        return serializers.PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """CRUD for Comment entity"""
    queryset = models.Comment.objects.order_by('creation_date')
    serializer_class = serializers.CommentSerializer
