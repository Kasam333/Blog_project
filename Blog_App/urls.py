from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),  # Home page for the blog
    path("profile/", views.profile, name="profile"),
    path('post/<int:pk>', PostDetailsViews.as_view(), name="post-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('post/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category-list/', CategoryListView, name='category-list'),
    path('category/<str:category_name>/', views.CategoryView, name='category'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]

# No need to add static or media handling here; it's already in the project-level urls.py
