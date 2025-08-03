from rest_framework import permissions

class CustomerPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('customers.view_customers')

        if request.method == 'POST':
            return request.user.has_perm('customers.add_customers')

        return False