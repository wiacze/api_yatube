from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.IsAuthenticated):
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
