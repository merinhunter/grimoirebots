from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(
        _("email address"),
        unique=True,
        help_text=_("Required. 254 characters or fewer."),
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )
