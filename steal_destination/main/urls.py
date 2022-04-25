from django.urls import path
from steal_destination.main.views.blog import BlogView, ArticleDetailsView, \
    CreateArticleView, EditArticleView, likes_article, DeleteArticleView
from steal_destination.main.views.comments import CreateCommentView, EditCommentView, DeleteCommentsView
from steal_destination.main.views.destinations import CreateDestinationView, DestinationsView, DestinationDetailsView, \
    EditDestinationView, DeleteDestinationView, likes_destination
from steal_destination.main.views.gallery import blog_view, detail_view
from steal_destination.main.views.generic import *

urlpatterns = [

    path('', HomePageView.as_view(), name='index'),
    path('destinations/', DestinationsView.as_view(), name='destinations'),
    path('destination/<int:pk>/', DestinationDetailsView.as_view(), name='destination'),
    path('destination/add/', CreateDestinationView.as_view(), name='create destination page'),
    path('destination/<int:pk>/liked/', likes_destination, name='likes destination'),
    path('destination/<int:pk>/edit/', EditDestinationView.as_view(), name='edit destination page'),
    path('destination/<int:pk>/delete/', DeleteDestinationView.as_view(),
         name='delete destination page'),
    path('destination/<int:pk>/comment/', CreateCommentView.as_view(), name='add comment'),
    path('comment/<int:pk>/edit/', EditCommentView.as_view(), name='edit comment'),
    path('comment/<int:pk>/delete/', DeleteCommentsView.as_view(), name='delete comment'),

    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/add/', CreateArticleView.as_view(), name='article create'),
    path('article/<int:pk>/', ArticleDetailsView.as_view(), name='article details'),
    path('article/<int:pk>/liked/', likes_article, name='likes article'),
    path('article/<int:pk>/edit/', EditArticleView.as_view(), name='edit article'),
    path('article/<int:pk>/delete/', DeleteArticleView.as_view(),
         name='delete article'),

    path('gallery/', blog_view, name='gallery'),
    path('gallery/<int:id>/', detail_view, name='gallery detail'),

]

import steal_destination.accounts.signals
