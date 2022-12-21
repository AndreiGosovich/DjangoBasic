__all__ = ['CourseFeedback']

from django.db import models

from django.contrib.auth import get_user_model

from django.utils.translation import gettext_lazy as _

class CourseFeedback(models.Model):
    RATING = ((5, "⭐⭐⭐⭐⭐"), (4, "⭐⭐⭐⭐"), (3, "⭐⭐⭐"), (2, "⭐⭐"),
    (1, "⭐"))
    course = models.ForeignKey(
        'mainapp.Courses', on_delete=models.CASCADE, verbose_name = _("Course")
    ) 
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, verbose_name = _("User")
    ) 
    feedback = models.TextField(
    default=_("No feedback"), verbose_name = _("Feedback")
    ) 
    rating = models.SmallIntegerField(
    choices=RATING, default=5, verbose_name = _("Rating")
    ) 
    created = models.DateTimeField(auto_now_add=True, verbose_name = _("Created"))
    deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.course} ({self.user})"