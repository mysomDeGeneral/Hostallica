from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from .models import Student
from django.urls import reverse_lazy 

class StudentCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Student
        fields = (
            "name",
            "username",
            "phone",
            "program",
            "picture",
        )

'''
class StudentChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()
    class Meta(UserChangeForm.Meta):
        model = Student
        fields = ('name',
                   'username', 
                   'phone', 
                   'program',
                    'picture',
                    
                     )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].help_text = ("Raw passwords are not stored, so there is no way to see "
                                            "this user's password, but you can change the password "
                                            "using <a href=\"../password/\">this form</a>."
        ) % reverse_lazy('admin:auth_user_password_change', args=(self.instance.id,)) 
  ''' 