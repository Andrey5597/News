from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
# CRUD for Post entity + PATCH for increase amount_upvote counter
router.register('post', views.PostViewSet, basename='post')
# CRUD for Comment entity
router.register('comment', views.CommentViewSet, basename='comment')

urlpatterns = router.urls
