from django.db import models


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    contents = models.TextField(blank=False, null=False)


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_id = models.ForeignKey("Post", related_name="post", on_delete=models.CASCADE, db_column="post_id")
    contents = models.TextField(blank=False, null=False)
