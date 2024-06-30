from django.db import models


class Study(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    serial = models.PositiveIntegerField(verbose_name="Порядковый номер")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name, self.serial

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ['serial']
