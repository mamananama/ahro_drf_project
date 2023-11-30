from django.db import models
from django.urls import reverse


class Schedule(models.Model):
    owner = models.ForeignKey(
        "accounts.CustomUser", verbose_name=("owner"), on_delete=models.CASCADE)
    title = models.CharField(max_length=64, blank=False, null=False)
    start_at = models.DateTimeField(blank=False, null=False)
    end_at = models.DateTimeField()
    content = models.TextField()

    class Meta:
        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Schedule_detail", kwargs={"pk": self.pk})
