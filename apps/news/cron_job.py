from apps.news import models


def refresh_amount_of_upvotes():
    models.Post.objects.update(amount_of_upvotes=0)
