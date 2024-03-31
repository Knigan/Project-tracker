from django.db import models
from tasks.models import Project, Task

# Create your models here.

class BugReport(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    project = models.ForeignKey(
        Project,
        related_name = 'bugreports',
        on_delete = models.CASCADE
    )

    task = models.ForeignKey(
        Task,
        related_name = 'bugreports',
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )

    STATUS_CHOICES = [
        ("New", "Новый"),
        ("In progress", "В работе"),
        ("Completed", "Завершён"),
    ]

    status = models.CharField(
        max_length = 50,
        choices = STATUS_CHOICES,
        default = "New"
    )

    PRIORITY_CHOICES = [
        (1, "Very high"),
        (2, "High"),
        (3, "Mediocre"),
        (4, "Low"),
        (5, "Very low")
    ]

    priority = models.IntegerField(
        choices = PRIORITY_CHOICES,
        default = 5
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class FeatureRequest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    project = models.ForeignKey(
        Project,
        related_name = 'feature_requests',
        on_delete = models.CASCADE
    )

    task = models.ForeignKey(
        Task,
        related_name = 'feature_requests',
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )

    STATUS_CHOICES = [
        ("Review", "Рассмотрение"),
        ("Accepted", "Принято"),
        ("Rejected", "Отклонено"),
    ]

    status = models.CharField(
        max_length = 50,
        choices = STATUS_CHOICES,
        default = "Review"
    )

    PRIORITY_CHOICES = [
        (1, "Very high"),
        (2, "High"),
        (3, "Mediocre"),
        (4, "Low"),
        (5, "Very low")
    ]

    priority = models.IntegerField(
        choices = PRIORITY_CHOICES,
        default = 5
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

