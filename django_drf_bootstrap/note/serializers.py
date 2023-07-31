from rest_framework import serializers

from .models import Note
from ..permissions import WriteOnceMixin

class NoteSerializer(WriteOnceMixin, serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ('id', 'user', 'created_at')
        write_once_fields = ('name',)
