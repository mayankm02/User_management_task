from rest_framework import generics, permissions
from .models import Blog
from .serializers import BlogSerializer
from .permissions import IsOwnerOrAdmin

class BlogListCreateView(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # if admin -> show all blog
        if user.is_staff or getattr(user, 'is_admin', False):
            return Blog.objects.all().order_by('-created_at')
        # if normal user -> show his blog only
        return Blog.objects.filter(author=user).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
