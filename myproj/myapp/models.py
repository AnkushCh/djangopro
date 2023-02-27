
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import Group


class Client(User):
    class Meta:
        proxy = True

class Employee(User):
    class Meta:
        proxy = True

class Manager(User):
    class Meta:
        proxy = True

GROUP_CHOICES = (
    ('Client', 'Client'),
    ('Employee', 'Employee'),
    ('Manager', 'Manager'),
)

for choice in GROUP_CHOICES:
    name = choice[0]
    if not Group.objects.filter(name=name).exists():
        Group.objects.create(name=name)


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    task_date = models.DateField()
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('complete', 'Complete'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

