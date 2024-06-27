from django.db import models


class Survey(models.Model):
    answers = models.JSONField()

    def __str__(self):
        return str(self.pk)
