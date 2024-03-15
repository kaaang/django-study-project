from django.db import models
import uuid

class UserModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=False, null=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    age = models.PositiveIntegerField(blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "유저 정보"
        verbose_name_plural = "유저 정보"
        ordering = ["name", "age"]
