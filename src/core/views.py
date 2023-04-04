from rest_framework import viewsets, permissions
from .serializers import PostSerializer
from .models import Post
__all__ = [
    'PostViewSet',
]


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]
