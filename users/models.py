from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Custom user model for extension."""

    def __str__(self):
        return self.email
