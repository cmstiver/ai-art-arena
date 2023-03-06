from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from AIArtArena import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = format_suffix_patterns([
    path('posts/', views.PostList.as_view(), name='post-list'),
])

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
