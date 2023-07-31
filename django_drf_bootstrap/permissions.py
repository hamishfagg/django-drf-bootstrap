import rest_framework.permissions as default_permissions
from django.contrib.auth import get_user_model


# Allows permission if the user is not editing an object
class ReadOnly(default_permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in default_permissions.SAFE_METHODS


# Checks if user is the owner (via 'user_id' field) of an object
# This permission implicitly alllows authed users to CREATE an object.
# So write your permissions_classes carefully.
class IsOwner(default_permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if type(obj) == get_user_model():
            return obj.pk == request.user.id
        return obj.user_id == request.user.id  # TODO: Check that user_id field exists
    

class WriteOnceMixin:
    """Adds support for write once fields to serializers.

    To use it, specify a list of fields as `write_once_fields` on the
    serializer's Meta:
    ```
    class Meta:
        model = SomeModel
        fields = '__all__'
        write_once_fields = ('collection', )
    ```

    Now the fields in `write_once_fields` can be set during POST (create),
    but cannot be changed afterwards via PUT or PATCH (update).
    Inspired by http://stackoverflow.com/a/37487134/627411.
    """

    def get_extra_kwargs(self):
        extra_kwargs = super().get_extra_kwargs()

        # If the obj instance is set, this is an UPDATE operation
        if self.instance:
            return self._set_write_once_fields(extra_kwargs)

        return extra_kwargs

    def _set_write_once_fields(self, extra_kwargs):
        """Set all fields in `Meta.write_once_fields` to read_only."""
        write_once_fields = getattr(self.Meta, 'write_once_fields', None)
        if not write_once_fields:
            return extra_kwargs

        if not isinstance(write_once_fields, (list, tuple)):
            raise TypeError(
                'The `write_once_fields` option must be a list or tuple. '
                'Got {}.'.format(type(write_once_fields).__name__)
            )

        for field_name in write_once_fields:
            kwargs = extra_kwargs.get(field_name, {})
            kwargs['read_only'] = True
            extra_kwargs[field_name] = kwargs

        return extra_kwargs
