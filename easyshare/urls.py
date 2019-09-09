from django.urls import path

from . import views
from .views import postListview, postDetailview, postCreateview, postUpdateview, postDeleteview, UserpostListview


urlpatterns = [
    path('', postListview.as_view(), name='homepage'),
    path('user/<str:username>', UserpostListview.as_view(), name='user-posts'),
    path('post/<int:pk>/', postDetailview.as_view(), name='post_details'),
    path('post/<int:pk>/update/', postUpdateview.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', postDeleteview.as_view(), name='post_delete'),
    path('post/new/', postCreateview.as_view(), name='post_create'),
    path('about/', views.about, name='about'),


]
