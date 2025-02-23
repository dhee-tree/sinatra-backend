import uuid
from django.db import models
from User.models import CustomUser

# Create your models here.
class Organisation(models.Model):
    choices = (
        ("NGO","NGO"),
        ("Charity", "Charity")
    )
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=50, default="")
    type = models.CharField(max_length=50, choices=choices ,default="Charity")
    address = models.CharField(max_length=50, default="")
    address_line_one = models.CharField(max_length=50, default="")
    address_line_two = models.CharField(max_length=50, default="")
    address_line_county = models.CharField(max_length=50, default="")
    address_line_city = models.CharField(max_length=50, default="")
    address_line_postcode = models.CharField(max_length=20, default="")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='organisation')

    def __str__(self):
        return self.name
    
    @classmethod
    def get_user_organisation(cls, user):
        return cls.objects.filter(user=user)