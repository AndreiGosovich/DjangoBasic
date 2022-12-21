__all__ = ['News']

from django.db import models

from django.utils.translation import gettext_lazy as _

class NewsManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(deleted=False)


class News(models.Model):
    objects = NewsManager()

    title = models.CharField(max_length=256, verbose_name="Title")
    preambule = models.CharField(max_length=1024, verbose_name="Preambule")
    body = models.TextField(blank=True, null=True, verbose_name="Body")
    body_as_markdown = models.BooleanField(
        default=False, verbose_name="As markdown"
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Created", editable=False
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Edited", editable=False
    )
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk} {self.title}"

    def delete(self, *args):
        self.deleted = True
        self.save()


    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
        ordering = ("-created",)