from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

from django.urls import reverse_lazy
from django.utils.safestring import mark_safe

from django.views.generic import CreateView, UpdateView

from django.contrib.auth.mixins import UserPassesTestMixin

from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model

from authapp.forms.user_creation_form import CustomUserCreationForm
from authapp.forms.user_change_form import CustomUserChangeForm

import logging
logger = logging.getLogger(__name__)


class CustomLoginView(LoginView):

    def form_valid(self, form):
        logger.info("Страница: Вход")
        ret = super().form_valid(form)
        message = ("Login success!<br>Hi, %(username)s") % {
                "username": self.request.user.get_full_name()
                if self.request.user.get_full_name()
                else self.request.user.get_username()
            } 
        messages.add_message(self.request, messages.INFO, mark_safe(message))
        return ret

    def form_invalid(self, form):
        for _unused, msg in form.error_messages.items():
            messages.add_message(
                self.request,
                messages.WARNING,
                mark_safe(f"Something goes worng:<br>{msg}"),
            )
        return self.render_to_response(self.get_context_data(form=form))


class CustomLogoutView(LogoutView):
	def dispatch(self, request, *args, **kwargs):
		messages.add_message(self.request, messages.INFO, _("See you later!"))
		return super().dispatch(request, *args, **kwargs)


class RegisterView(CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("mainapp:main_page")



class ProfileEditView(UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm

    def test_func(self):
        logger.info("Страница: Редактирование профиля")
        return True if self.request.user.pk == self.kwargs.get("pk") else False

    def get_success_url(self):
        return reverse_lazy("authapp:profile_edit", args=[self.request.user.pk])