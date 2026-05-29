from django.core.exceptions import PermissionDenied


class UserIsOwnerMixin:
    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        if self.request.user == product.owner or self.request.user.has_perm("catalog.can_unpublish_product"):
            return product
        raise PermissionDenied
