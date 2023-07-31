# Django DRF Bootstrap

This Django project exists to make bootstrapping a rest API in django faster. Only two models exist:
- `User`
  - Has an email, username, and password
  - Unauthenticated people can create new users (pending email validation)
  - Users can reset their password, change email with verification (handled by Djoser, see below)
- `Note`
  - Represents a sticky-note. Has a name and content text, and a created datetime
  - Logged-in users can create notes, and edit the content of their own notes
  - Anyone can read all notes in the DB
  - Admins can edit all notes in the DB

The project includes a number of commonly-needed libraries and concepts already set up:
- Django Rest Framework installed/configured basically
- [Djoser library](https://djoser.readthedocs.io/en/latest/) used for token authentication and handling of email valdation/password reset. 
- Custom user model configured, ready for more fields to be added
- [DRF-Spectacular](https://drf-spectacular.readthedocs.io/en/latest/) set up to automatically generate swagger docs at `/api-docs`
- Custom permissions added for `IsOwner` and `ReadOnly`.
  - `IsOwner` allows users to create an object, and then only read/edit an object if they own it.
  - `ReadOnly` allows anyone to read an object, but not edit it.
  - Permissions can be composed with bitwise operators:
    ```python
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
    ```
- Write-once mixin added to allow only writing fields on object creation (then they become readonly)
  - Here, `name` can only be written when the object is created
    ```python
    class NoteSerializer(WriteOnceMixin, serializers.ModelSerializer):
        class Meta:
            model = Note
            fields = '__all__'
            read_only_fields = ('id', 'user', 'created_at')
            write_once_fields = ('name',)
    ```
  - This is useful e.g. when creating comment replies etc, where a user should be able to specify what they're replying to, but not change that later.

todo: email address in users table, email validation etc