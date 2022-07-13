from django.db import models


class Staff(models.Model):
    class PositionChoices(models.TextChoices):
        JUNIOR = 'JUNIOR'
        MIDDLE = 'MIDDLE'
        SENIOR = 'SENIOR'
        INTERN = 'INTERN'

    FIO = models.CharField(max_length=100)
    position = models.CharField(max_length=100, choices=PositionChoices.choices)
    date = models.DateField()
    salary = models.IntegerField(default=0)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.FIO
