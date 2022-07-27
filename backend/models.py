from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class Developer(models.Model):
    LANGUAGES = [
        ('py', 'Python'),
        ('cpp', 'C++'),
        ('cs', 'C#'),
        ('java', 'Java'),
        ('js', 'JavaScript'),
        ('other', 'Other'),
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    language = models.CharField(max_length=5, choices=LANGUAGES, default='other')

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Project(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0),])
    date_start = models.DateField()
    date_end = models.DateField()
    developer = models.OneToOneField(to=Developer, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name