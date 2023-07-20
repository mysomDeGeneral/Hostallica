from django.contrib.auth.forms import UserCreationForm
from backend.models import Student
#from django.contrib.auth.models import User

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


'''class SiguUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
        )'''