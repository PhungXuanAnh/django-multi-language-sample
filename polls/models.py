from django.db import models
from django.utils.translation import gettext_lazy as _

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name=_("Question name"))
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Question")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name=_("Choice name"))
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

    class Meta:
            verbose_name = _("Choice")
            verbose_name_plural = _("Choice")        