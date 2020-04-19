from django.contrib.auth.models import User


class EmailAuth:
    """Authenticate a user by an email"""

    def authenticate(self, username=None, password=None):
        """Get instance of user which is based off the email and verification of the password"""

        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """Django authentication system uses this to retrieve the user instance"""
        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
