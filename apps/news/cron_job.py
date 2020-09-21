from apps.news import models


def refresh_amount_of_upvotes():
    """
    Sets amount of upvotes every day at 00:00 AM to 0
    returns: None
    """
    models.Post.objects.update(amount_of_upvotes=0)
