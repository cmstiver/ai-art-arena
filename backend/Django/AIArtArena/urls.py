from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from AIArtArena import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('posts/<str:pk>', views.PostDetail.as_view(), name='post-detail'),
    path('posts/<str:pk>/like/', views.like_post, name="post-like"),
    path('my_posts/', views.UserPostList.as_view(), name="my-posts"),
    path('users/',
         views.UserList.as_view(),
         name='user-list'),
    path('users/<int:pk>/',
         views.UserDetail.as_view(),
         name='user-detail'),
    path('register/', views.RegisterUser.as_view()),

])

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
