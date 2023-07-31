from django.contrib.auth import get_user_model
from djoser import views
from drf_spectacular.utils import extend_schema, extend_schema_view

from .models import User
from .serializers import UserSerializer


@extend_schema_view(
    # list=extend_schema(exclude=True),  # Commented out to allow us to list other users
    # retrieve=extend_schema(exclude=True),  # Commented out to allow us to retrieve another user's details
    
    # Don't show endpoints to update/delete other users
    update=extend_schema(exclude=True),
    partial_update=extend_schema(exclude=True),
    destroy=extend_schema(exclude=True),
    me=[
        extend_schema(methods=['GET'], description='Get details of your account.'),
        extend_schema(methods=['PUT', 'PATCH'], description='Update details of your account.'),
        extend_schema(methods=['DELETE'], description='Close your account.'),
    ]
)
class UserViewSet(views.UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
