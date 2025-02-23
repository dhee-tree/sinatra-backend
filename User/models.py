import uuid
from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from django.db.models import Q
from django.shortcuts import get_object_or_404
from Skills.models import Skill

from Sinatra.storage_backends import PrivateMediaStorage


# Create your models here.
class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(
            Q(**{self.model.USERNAME_FIELD: username}) |
            Q(**{self.model.EMAIL_FIELD: username})
        )


class CustomUser(AbstractUser):
    age = models.IntegerField(default=18)
    created = models.DateTimeField(auto_now_add=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)

    image = models.FileField(storage=PrivateMediaStorage(), upload_to='profile/picture/', default='', blank=True)
    middle_name = models.CharField(max_length=50, default="", null=True, blank=True)
    nationality = models.CharField(max_length=50, default="")
    objects = CustomUserManager()
    phone_number = models.CharField(max_length=20, default="")
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    skills = models.ManyToManyField(Skill , related_name='users',blank= True)
    points = models.IntegerField(default=0)

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.username}"

    @classmethod
    def get_user_via_uuid(cls, user_uuid):
        return get_object_or_404(CustomUser, uuid=user_uuid)

    @classmethod
    def change_user_password(cls, user_uuid, new_password):
        user = get_object_or_404(CustomUser, uuid=user_uuid)
        user.set_password(new_password)
        user.save()

