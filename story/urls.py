from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/new/', views.post_new, name='post-new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post-edit'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/comment/<int:pk1>/reply', views.reply, name='reply'),
]