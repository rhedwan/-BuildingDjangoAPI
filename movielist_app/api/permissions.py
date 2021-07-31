from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        admin_permission = bool(request.user and request.user.is_staff)
        return request.method == "GET" or admin_permission

        # ALITER
        """ if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff) """



class ReviewUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request 
            return True
        else:
            # Check permissions for write request
            return obj.review_user == request.user

"""
LINKS: https://github.com/encode/django-rest-framework/blob/master/rest_framework/permissions.py

1. 'AdminOrReadOnly' class: This is used for allowing all methods for 'admin' only and 'GET' method is 
allowed for all other 'User'.
2. The methods should return True if the request should be granted access, and False otherwise
3. SAFE_METHODS has only the ('GET', 'HEAD', 'OPTIONS')
4. The 'request.method' is checking all the default method allowed by the view class

5. '.has_object_permission(self, request, view, obj)' is for checking the if the user accessing the
view was the author i.e creator. Making the user able to have access to 'editing' and the like.

['GET' ,'PUT','PATCH', 'PUT', 'DELETE']
"""