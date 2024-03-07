from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
import datetime

User = get_user_model()


class UserCreateForm(UserCreationForm):
    username = forms.CharField(
        label=_("username"), help_text="имя для входа на сайт, не менее 4 символов"
    )
    email = forms.EmailField(
        label=("адрес электронной почты"),
        max_length=254,
        help_text="может понадобиться для восстановления пароля",
    )
    first_name = forms.CharField(
        label=_("first name"),
        max_length=150,
        required=True,
        help_text="Как к Вам обращаться?",
    )
    phone_number = forms.CharField(
        label="телефон для связи",
        max_length=15,
        help_text="не обязательно, но может пригодится",
        required=False,
    )
    password1 = forms.CharField(
        label=_("password"), help_text="не менее 8 символов", widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="поджтверждение пароля",
        help_text="повторите пароль",
        widget=forms.PasswordInput,
    )
    sex = forms.ChoiceField(
        choices=User.SexChoices.choices,
        # required=False,
        label="ваш пол",
        widget=forms.RadioSelect(),
    )
    day_of_birth = forms.DateField(
        label="дата рождения",
        widget=forms.DateInput(
            attrs={"type": "date", "max": datetime.datetime.now().date().strftime("%Y-%m-%d")}
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "phone_number",
            "day_of_birth",
            "sex",
            "password1",
            "password2",
        )


class ChangeUserInfoForm(forms.ModelForm):
    phone_number = forms.CharField(
        label="телефон для связи", max_length=30, required=False
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "first_name", "phone_number")


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(),
    )
    password = forms.CharField(
        label=_("password"),
        widget=forms.PasswordInput(),
    )
