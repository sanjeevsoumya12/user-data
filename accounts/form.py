from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")
        
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        # password2 = self.cleaned_data.get("password2")
        contains_digit=any(map(str.isdigit,password1))
        if not contains_digit:
            self.add_error("password2","password must contains digit")
        return password1




# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError(
#                 self.error_messages['password_mismatch'],
#                 code='password_mismatch',
#             )
#         return password2
