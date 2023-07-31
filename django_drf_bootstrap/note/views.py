from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Note
from .serializers import NoteSerializer
from ..permissions import IsOwner, ReadOnly

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    # Compose permissions so that:
    # Admins:
    #   - Can read any note
    #   - Can edit any note
    # Logged-in users:
    #   - Can read any note
    #   - Can edit only their own notes
    # Anonymous users:
    #   - Can't read or edit any notes
    permission_classes = [IsAdminUser | IsOwner | (IsAuthenticated & ReadOnly)]


    # This forces the 'user' field to be set to the currently logged-in user when a note is created.
    # This makes sure that users can't make notes for other users
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
