from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from AIArtArena import views


urlpatterns = format_suffix_patterns([
    path('posts/', views.PostList.as_view(), name='post-list'),
])
