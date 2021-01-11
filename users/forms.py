from django.forms import ValidationError, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from bootstrap_datepicker_plus import  DatePickerInput
User = get_user_model()


class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'photo', 'phone_number', 'email',)


class PatientSignUpForm(UserCreationForm):
    # gender = forms.CharField(widget=forms.CharField(attrs={'placeholder':'Enter Your Gender'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
              'phone_number', 'gender', 'id_no',)

    def clean(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError('A user with this email already exists.')
        return self.cleaned_data
