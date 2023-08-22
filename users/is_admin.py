from .models import AdminUser, NormalUser

def is_admin(user):
    try:
        admin_user = AdminUser.objects.get(user=user)
        return True
    except AdminUser.DoesNotExist:
        return False