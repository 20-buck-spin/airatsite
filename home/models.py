from django.db import models


# Create your models here.
class SolvedCase(models.Model):
    title = models.TextField(verbose_name="Тема")
    date = models.DateField(auto_now_add=False, verbose_name="дата")
    description = models.TextField(verbose_name="Описание")
    is_published = models.BooleanField(verbose_name="Опубликоано")

    class Meta:
        verbose_name = "Успешный Кейс"
        verbose_name_plural = "Успешные Кейсы"

    def __str__(self):
        return self.title


def solved_case_file_upload(instance, filename):
    return "user_{0}/{1}".format(instance.case.title, filename)


class SolvedCaseFile(models.Model):
    case = models.ForeignKey(SolvedCase, on_delete=models.CASCADE, verbose_name="Кейс")
    name = models.CharField(max_length=255, verbose_name="Название")
    file = models.FileField(upload_to=solved_case_file_upload, verbose_name="Файл")

    class Meta:
        verbose_name = "Приложение к Р.К."
        verbose_name_plural = "Приложения к Р.К."
