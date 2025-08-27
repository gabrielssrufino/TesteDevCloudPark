from rest_framework import generics
from django.contrib.auth import get_user_model
from . import serializers

User = get_user_model()


class UserListView(generics.ListAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return User.objects.filter(groups__name="Tecnico")


class UserCreateView(generics.CreateAPIView):
    permission_classes = []

    serializer_class = serializers.UserCreateSerializer
