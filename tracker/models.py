from django.db import models

class Expense(models.Model):
    title = models.CharField(max_length=120)
    amount = models.FloatField()
    category = models.CharField(max_length=60, blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.title
