from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField(max_length=128)
    creation_date = models.DateField(auto_now_add=True)
    amount_of_upvotes = models.PositiveSmallIntegerField(default=0)
    author_name = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return f'Post {self.pk}'


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_comments'
    )
    author_name = models.CharField(max_length=50, default='')
    content = models.CharField(max_length=200)
    creation_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return f'Comment {self.pk}'
