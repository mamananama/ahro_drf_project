from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        "accounts.CustomUser", verbose_name="author", on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=128, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    schedule = models.ForeignKey("schedule.Schedule", verbose_name=(
        "schedule"), on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})
